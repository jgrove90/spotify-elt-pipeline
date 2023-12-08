# python base image
FROM public.ecr.aws/emr-on-eks/spark/emr-6.15.0:emr-on-eks-6.15.0

USER root

# keeps python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# dependency file 
COPY requirements.txt .

# install python dependencies 
RUN pip3 install -r requirements.txt

# copy src folder over with appuser ownership
COPY --chown=hadoop:hadoop ./src .

USER hadoop:hadoop