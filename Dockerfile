FROM jenkins/jenkins:latest-jdk17
# if we want to install via apt
USER root
RUN apt-get update && apt-get install -y python3 python3-pip

#RUN curl -o allure-commandline-2.20.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.20.0/allure-commandline-2.20.0.tgz && tar -zxvf allure-commandline-2.20.0.tgz -C / && ln -s /allure-commandline-2.20.0/bin/allure /bin/allure
#ENV PATH="$PATH:/allure-2.20.0/bin"

WORKDIR /code
COPY ./code /code
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# drop back to the regular jenkins user - good practice
USER jenkins

RUN jenkins-plugin-cli --plugins allure-jenkins-plugin:2.30.3
