#!/usr/bin/env python3

env = {
	"TARGET_ADDRESS": input("Target address: ") or "pigeon9000.local",
	"TARGET_BIN_LOCATION": input("Target binary location: ") or "'~'",
	"TARGET_USER": input("Target user: ") or "philip",
	"VM_ADDRESS": input("Virtual machine address: ") or "localhost",	
	"VM_PORT": input("Virtual machine port: ") or "2222",
	"VM_PROJECT_LOCATION": input("Virtual machine project location: ") \
							or "/media/sf_9000d",
	"VM_USER": input("Virtual machine user: ") or "philip",
	"TARGET": input("Target arch: ") or "armv7",
	"CONFIGURATION": input("Configuration: ") or "debug"
}

text = ""

for key in env:
	text += "export %s=%s\n" % (key, env[key])


open(".env", "w").write(text)