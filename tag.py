import os, sys, re

VERSION_REGEX = r'v[0-9]+\.[0-9]+\.[0-9]+'

def isValidTag(tag):
	if tag is None:
		return False
	if tag == "":
		return False

	regex = re.compile(VERSION_REGEX)
	if regex.match(tag):
		return True

	print "WARNING: Ignoring invalid tag: " + tag
	return False

def versionTuple(v):
	components = v.replace("v", "").split(".")
	if not isValidTag(v):
		raise ValueError('Invalid version detected: ' + v)

	version = tuple(map(int, components))
	return version

def versionTupleToString(v):
	return "v{}.{}.{}".format(v[0], v[1], v[2])

def scanCurrentBranchTagsAndGetBiggestVersion():
	log_for_current_branch = os.popen('git log --decorate --pretty=oneline').read()
	all_tags = []
	log_tag_version_regex = r'tag: ({})'.format(VERSION_REGEX)
	for line in log_for_current_branch.split("\n"):
		for match in re.finditer(log_tag_version_regex, line):
			all_tags.append(match.group(1))

	biggest_tag_version = None
	for tag in all_tags:
		if isValidTag(tag):
			tag_version = versionTuple(tag)
			if biggest_tag_version is None or biggest_tag_version < tag_version:
				biggest_tag_version = tag_version
	return biggest_tag_version

def getBiggestVersionTagForCurrentBranch():
	last_tag = os.popen("git describe --abbrev=0 --tags").read().replace("\n", "")
	if not isValidTag(last_tag):
		raise ValueError('Cannot read the last tag version. Please use a valid tag format (v1.2.3) for the last tagged commit in current branch')

	current_version = versionTuple(last_tag)
	biggest_version_for_branch = scanCurrentBranchTagsAndGetBiggestVersion()
	if biggest_version_for_branch is None:
		raise ValueError('Cannot read any tag from current branch.')

	if current_version != biggest_version_for_branch:
		print "WARNING: The latest tag ({}) is not the biggest version in branch ({}). Using biggest version.".format(last_tag, versionTupleToString(biggest_version_for_branch))

	return biggest_version_for_branch

def createNewTagOnCurrentHeadIfNotTagged(current_tag, new_tag):
	tag_in_head = os.popen("git tag --contains HEAD").read().replace("\n", "")
	if tag_in_head != "":
		print 'No new tag. HEAD already tagged as {}'.format(tag_in_head)
	else:
		print "Creating new tag: {} (previous tag for branch: {})".format(new_tag, current_tag)
		os.popen("git tag {} HEAD".format(new_tag))

def composeCandidateTagFromArguments():
	tag = None
	if len(sys.argv) > 1 and sys.argv[1] == "bump-minor":
		tag = (current_tag[0], current_tag[1] + 1, 0)
	elif len(sys.argv) > 1 and sys.argv[1] == "bump-major":
		tag = (current_tag[0] + 1, 0, 0)
	else:
		tag = (current_tag[0], current_tag[1], current_tag[2] + 1)
	return tag

#run!
current_tag = getBiggestVersionTagForCurrentBranch()
new_version_tag = composeCandidateTagFromArguments()
createNewTagOnCurrentHeadIfNotTagged(versionTupleToString(current_tag), versionTupleToString(new_version_tag))
