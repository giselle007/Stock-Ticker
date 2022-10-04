# Stock-Ticker
This web app will display the closing price for the selected day and stock symbol. 


### Prerequisites to run this webapp you must have the following requirements
- Kubernetes
- Minikube (optional)
- Docker
- Python

### Instructions to deploy the stock-ticker webapp
##### Step 1: Clone Repo
<ol>
<li>clone the git repo into the desired folder using the command <code>git clone https://github.com/giselle007/Stock-Ticker.git</code></li>
</ol>

##### Step 2: Build and Deploy

>Note: Since the docker image has already been built the following step is optional

###### Step 2 (OPTIONAL): Build local docker file
<ol>
<li>Open your command window/cli termal</li>
<li>Change into the Stock-Ticker directory with the command <code>cd Stock-Ticker</code></li>
<li>Build a local docker file using the docker file in this repo by running the following command <code>docker build -t [IMAGE_NAME]:[IMAGE_VERSION] .</code></li>
<li>Update the pod.yaml file line 11 and update the image to your local image <code>image: <IMAGE_NAME>:<IMAGE_VERSION></code></li>
<li>Continue to step 2 deploy</li>
</ol>
  
##### Step 2: Deploy
<ol>
<li>Open your command window/cli termal</li>
<li>Change into the Stock-Ticker directory with the command <code>cd Stock-Ticker</code></li>
<li>Run the following command to deploy your kubernetes pod, service, and secret <code>kubectl create -f pod.yaml</code></li>
</ol>
  
##### Step 3: Verify Locally
>Note: You must have minikube running locally
<ol>
<li>Open your command window/cli termal</li>
<li>The default url to verify locally is http://127.0.0.1:51768/ in the event that this does not work run the command <code>minikube service stockticker-service --url</code> to view your localhost</li>
</ol>
