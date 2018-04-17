#!/usr/bin/python
#coding=utf-8

import sys
import os
import re

MAX_LENGTH = 100
pattern = r'^(?:fixup!\s*)?(\w*)(\(([\w\$\.\*/-]*)\))?\: (.*)$'
TYPES = ('feat', 'fix', 'docs', 'style', 'refactor', 'perf', 'test', 'chore', 'revert')

def validateMsglen(msg):
	if len(msg) > 100:
		print "msg length longer than " +  MAX_LENGTH
		sys.exit(1)

def validateMsgType(msg_type):
    if msg_type not in TYPES:
    	print "msg type error"
    	sys.exit(1)

def validateMsgFormat(msg):
	commit_msg_match = re.match(pattern, msg)
	if commit_msg_match:
		validateMsgType(commit_msg_match.group(1))
	else:
		print "commit msg subject: " + "\'" + msg + "\'" + " does not match \"<type>(<scope>): <subject>\" " 
		sys.exit(1)

def getMsgHead(old_value, new_value):
	#print old_value
	#print new_value
	#删除分支时，新的引用为40个0
	if new_value == "0000000000000000000000000000000000000000":
		git_command = "git log " + old_value + " -1 --pretty=\"%s\""
	else:
		git_command = "git log " +  new_value + " -1 --pretty=\"%s\""
	commit_msg_head = os.popen(git_command).readlines()[0].strip()
	return commit_msg_head

def main():
    #ref_name = sys.argv[1]
	old_value = sys.argv[2]
	new_value = sys.argv[3]
	msg_head = getMsgHead(old_value, new_value)
	validateMsglen(msg_head)
	validateMsgFormat(msg_head)


if __name__ == "__main__":
    main()
