import os, sys, re

def isValidTag(tag):
	if tag is None:
		return False
	if tag == "":
		return False

	regex = re.compile(r'v[0-9]+\.[0-9]+\.[0-9]+(\.[0-9]+)?$')
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
	return "v" + str(v[0]) + "." + str(v[1]) + "." + str(v[2])

def scanAllTagsAndGetBiggestVersion():
	all_tags = os.popen("git tag").read().split("\n")
	biggest_tag_version = None
	for tag in all_tags:
		if isValidTag(tag):
			tag_version = versionTuple(tag)
			if biggest_tag_version is None or biggest_tag_version < tag_version:
				biggest_tag_version = tag_version
	return biggest_tag_version

def getVersionTagForCurrentBranch():
	last_tag = os.popen("git describe --abbrev=0 --tags").read().replace("\n", "")
	if not isValidTag(last_tag):
		raise ValueError('Cannot read the last tag version. Please use a valid tag format (v1.2.3) for the last tagged commit in current branch')

	current_version = versionTuple(last_tag)
	biggest_version = scanAllTagsAndGetBiggestVersion()
	if biggest_version is None:
		raise ValueError('Cannot read any tag from current repo.')

	if current_version != biggest_version:
		print "WARNING: The latest tag (" + last_tag + ") is not the biggest version (" + versionTupleToString(biggest_version) + ")"
	
	return current_version

def createNewTagOnCurrentHeadIfNotTagged(current_tag, new_tag): 
	tag_in_head = os.popen("git tag --contains HEAD").read().replace("\n", "")
	if tag_in_head != "":
		print 'No new tag. HEAD already tagged as ' + tag_in_head
	else:
		print "Creating new tag: " + new_tag + " (previous tag for branch: " + current_tag + ")"
		os.popen("git tag " + new_tag + " HEAD")


#run!
current_tag = getVersionTagForCurrentBranch()
new_version_tag = (current_tag[0], current_tag[1], current_tag[2] + 1)
createNewTagOnCurrentHeadIfNotTagged(versionTupleToString(current_tag), versionTupleToString(new_version_tag))
