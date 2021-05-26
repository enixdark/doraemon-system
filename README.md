## Doraemon System 

Doraemon system have't mean , it's simple a joke name that we think it based character doraemon. 
However your duty 's solve all quizs.

Lesson 1:

We provide for you a template code with python language (we choose python because it mainly language in our company)
This project in this lesson use simple flask demo with a function upload file and word count via rest api.

let install app and run server, then use rest call api with command:

```bash
curl -X POST -H "Content-type: application/json" 127.0.0.1:5000/file -d "{\"path\": \"your_data_file\"}"
```

A output folder with result file 'll appear with list word and total their number.

Now, in this lesson, as a cloud app, we 're going setup and deploy run on cloud environment so we need you to find at least 3 missing in project and improve, then let containerize this project.

Note: There 're more 3 missing


Lesson 2:

- Based on lesson 1, we need processing a large file data but my computer/service ( in your side are containers ) has limited,
I have only allocate 100mcpu and 100mb Ram for this app, however my file maybe large to 1-10GB, so let use a method/logic that my service can processing a large file data without OOM kill app by over cpu or ram.

We provide for you a link for large data https://docs.google.com/file/d/0B0i0Mek13ZjpeTZiSjI5bkF2N0k

download that data, extract then run unique a container/pod/service with limit resource 100mcpu and 100mb ram 
then load all data via rest api like lesson 1. Remember that, We only need you give a algorithm or logic for solving this problem without demo app, however you can try for 1-10-100-1000Mb or full data for testing your logic.


Lesson 3:

- Now, we need enhance performance of service for processing faster, so you can scale app more than with scale up and scale out
so, let modify app from lesson 1 or 2. Nextly, you can use tool or trick to monitoring app and collect metric about cpu and ram or request and save to any storage that you are good. after storing metrics, let write logic to analysis and decide for auto scale up/out
in realtime.

Lesson 4: ( Option )

- Now, As as devops or ci/cd engineer , let's intergrate all and setup deploy this app to any server/cloud.


Note: for candidates, we always want to anyone with growth mindset, you can find any solutions for improving this app with any technologies.

