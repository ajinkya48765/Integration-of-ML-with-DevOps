# How to integrate Machine Learning with DevOps

## Hello everyone, Do you ever ask yourself the question "Can I integrate Machine Learning with DevOps ?" So I am here with the answer and answer is yes, We can integrate ML with DevOps and it is collectively called as MLOps. We can achive MLOps in various ways and for various use cases. This article will explain you one of them.

### Problem Overview :
1. Create docker container image that has python installed in it along with all the essential libraries required for training Machine learning model.
2. Create number of jobs in jenkins to test , notify , rebuild , tweak the machine learning model in order to get desired accuracy.

### Solution Overview :

We are going going to build chain of jobs here in order to get desired accuracy for given dataset but before going ahead we have to create a Dockerfile which will create image with required configurations.

* Job 1 : Job 1 will keep an eye on github repository as soon as developer push something there this job will automatically copy everything in the folder of my base os.(I am using RHEL 8 as my base os (VM)).

* Job 2 : Success of Job 1 will trigger job to this job will launch docker container which is workspace for Jenkins.

* Job 3 : After successfully launching the OS Jenkins will trigger this job. This job will search for file which is pushed by developer and has a main code to train model. (main.py in my case)

* Job 4 : I have created Job 4 to notify developer that main.py file has some errors due to which job 3 failed.

* Job 5 : If main.py runs successfully but give less accuracy than what developer desire then jenkins should automatically tweak something and by various hit and trials will try to increase the accuracy. In order to achive this thing developer will push one more file along with main.py that is rebuild.py. This will help jenkins to take tests and build model again and again till desired accuracy is achived.

* Job 6 : This job is success notifier as soon as jenkins succeed in achieving desired accuracy it will notify developer about success of the model and accuracy achieved.

* Job 7 : This job is again failure notier but now it will notify on failure of rebuild.py file.

* Job 8 : Job 8 will be monitoring job. It will keep an eye on running container. If it found container crashed it will immediately launch new container with same configuration.


## for more details

### chekout my article on LinkedIn
[click here](https://www.linkedin.com/posts/ajinkya-khandave_machineabrlearning-devops-problemstatement-activity-6668678518643281920-EBHv)
