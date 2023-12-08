#!/bin/bash

# pull emr-on-eks image
docker pull public.ecr.aws/emr-on-eks/spark/emr-6.15.0:latest

# build custom emr-on-eks image
docker docker build -t spotify-elt . 