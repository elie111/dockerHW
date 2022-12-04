 <h1 align="center">Fursa HW4 Docker Final Task</h3>
  <h1 align="center">Elie Haddad</h3>
  
<p align="center" >
  <img src="https://logos-world.net/wp-content/uploads/2021/02/Docker-Symbol.png" alt="drawing" style="width:200px;"/>
</p>

#### **To run the project:**
>1. Clone:
git Clone https://github.com/elie111/dockerHW.git

> 2. Build:
docker compose up

> 3. open:
http://localhost:8000/

> 4. stop:
docker compose down


### **python web Application**
*  I built a python web application that shows the live price of bitcoin in USD and the average price of the last ten minutes, I used flask framework and redis database here is an example of what we got:

<p align="center" >
  <img src="/Images/bitprice.png" alt="drawing" style="width:700px;"/>
</p>


### **Jenkins pipeline with docker and github**

* We created a jenkins [pipeline](https://github.com/elie111/dockerHW/blob/main/Jenkinsfile). that creates and pushes the generated Web application Docker image to Docker Hub,
  And we connected the github account to jenkins, and added a Jenkinsfile to our repository and ran the script with the "pipeline script from SCM" option.

<p align="center" >
  <img src="/Images/blueocean.png" alt="drawing" style="width:700px;"/>
</p>

  #### **clone Stage**:
  > We cloned the project: git branch: "main",url:'https://github.com/elie111/dockerHW.git'
  #### **Login Stage**:
  > We logged in to dockerhub: echo $DOCKERHUB_CREDENTIALS_PSW |  docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
  #### **Build image Stage**:
  > We built the image: docker build -t eliehadd/dockerhw:latest . 
  #### **Push image Stage**:
  > We pushed the built image to dockerhub: docker push eliehadd/dockerhw
  #### **Post Actions Stage**:
  > we logged out of dockerhub: docker logout
  #### **Slack Notification Stage**: 
  > And finally we sent a message on a slack channel we created to inform us that the image has been built and pushed to dockerhub

<p align="center" >
  <img src="/Images/slack.png" alt="drawing" style="width:700px;"/>
</p>

<p align="center" >
  <img src="/Images/docker.png" alt="drawing" style="width:700px;"/>
</p>

<p align="center" >
  <img src="/Images/output.png" alt="drawing" style="width:700px;"/>
</p>
