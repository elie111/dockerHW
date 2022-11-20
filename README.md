 <h1 align="center">Fursa HW4 Docker Closing Task</h3>
  <h1 align="center">Elie Haddad</h3>
  
<p align="center" >
  <img src="https://logos-world.net/wp-content/uploads/2021/02/Docker-Symbol.png" alt="drawing" style="width:200px;"/>
</p>

#### **To run the project:**
>1. Clone:
git Clone https://github.com/elie111/JenkinsHW.git

> 2. Build:
docker compose up

> 3. open:
http://localhost:8000/

> 3. stop:
docker compose down


### **python Application**
*  I build a python web application that displays the live price of bitcoin in USD and the average of the last ten minutes, I used flask framework and redis database here is an example of what we got:

<p align="center" >
  <img src="/Images/newshtml.png" alt="drawing" style="width:700px;"/>
</p>


### **Jenkins pipeline with docker and github**

* We created a jenkins [pipeline](https://github.com/elie111/dockerHW/blob/main/Jenkinsfile). that creates and pushes the generated Web application Docker image to Docker Hub,
  And we connected the github account to jenkins, and added a Jenkinsfile to our repository and ran the script with the "pipeline script from SCM" option.

<p align="center" >
  <img src="/Images/blueocean.png" alt="drawing" style="width:700px;"/>
</p>

  #### **clone Stage**:
  > We cloned the project: git branch: "main",url:'https://github.com/elie111/JenkinsHW.git'
  #### **Login Stage**:
  > We cloned the project: git branch: "main",url:'https://github.com/elie111/JenkinsHW.git'
  #### **Build image Stage**:
  > We built the project using the command: mvn clean install assembly:single 
  #### **Push image Stage**:
  > We archived the jar file: archiveArtifacts artifacts: '**/*.jar'
  #### **Post Actions Stage**:
  >  We ran the jar file that was created from the building stage, which ran the server in the background: 
  > java -jar target/simplehttpserver-1.0-SNAPSHOT-jar-with-dependencies.jar & 
  #### **Slack Notification Stage**: 
  > And finally we sent a message on a slack channel we created to inform us that the project has been built and deployed

<p align="center" >
  <img src="/Images/slack.png" alt="drawing" style="width:700px;"/>
</p>

<p align="center" >
  <img src="/Images/output.png" alt="drawing" style="width:700px;"/>
</p>
