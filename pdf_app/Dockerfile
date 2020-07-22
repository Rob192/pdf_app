FROM continuumio/miniconda3

WORKDIR usr/src/pdf_app
RUN apt-get update
ADD environment.yml environment.yml
ADD requirements.txt requirements.txt

RUN conda env create -f environment.yml
ENV PATH /opt/conda/envs/dash_pseudo_app/bin:$PATH
RUN /bin/bash -c "source activate dash_pseudo_app"
COPY . .
