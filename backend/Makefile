###########################################################
#   _______            _____ _    _____          _        #
#  |__   __|          |  __ (_)  / ____|        | |       #
#     | |_      _____ | |__) |  | |     ___   __| | ___   #
#     | \ \ /\ / / _ \|  ___/ | | |    / _ \ / _` |/ _ \  #
#     | |\ V  V / (_) | |   | | | |___| (_) | (_| |  __/  #
#     |_| \_/\_/ \___/|_|   |_|  \_____\___/ \__,_|\___|  #
#                                                         #
#           Generic Dockerized Project MakeFile           #
###########################################################
##### Things that you should set up...

###     DEPLOYMENT NAME: This defines what the deployed app will be called, it's subdomain.
#		    By default, this is the projects name, you can override this like so:
#			DEPLOY_NAME="gths-attendance-api"

DEPLOY_NAME=$(shell basename $$CI_PROJECT_DIR)

###     HOST_x: This defines the addresses / hostnames of the destination dokku paas servers to deploy to.
#			Make sure you have set up your ssh keys properly before building!
#			HOST_CLUBHOUSE=docker.mypaas.com

HOST_DEV=twopico.de
HOST_PROD=

######################################################################################################

###     Automatically derived variables. You probably do not need to modify these.
#       $$DOCKER_REGISTRY is a global environment variable on the runner, override if required.

REPO_VERSION=$(shell git describe --dirty --always)
ARTIFACT_URL=$(shell echo $$DOCKER_REGISTRY)/$(shell tpci-get-artifact-name $$CI_PROJECT_DIR)

######################################################################################################

.PHONY: docker-build docker-push test install_precommit

test:
	flake8
	python test.py

install_precommit: 
	echo '#!/bin/sh\ngit stash -q --keep-index\nmake test\nRESULT=$$?\ngit stash pop -q\nexit $$RESULT\n' > .git/hooks/pre-commit;
	chmod +x .git/hooks/pre-commit;

##########################################################################################
# Deployment Magic
##########################################################################################

deploy_master:
	echo "Deployment not configured.";

deploy_production:
	echo "Deployment not configured.";


