
<h1 style="text-align:centre; width: 100vw; color: red;">Relax Teacher</h1><hr>

<h1>Motive</h1>
<p>My inspiration came from the aftermath of the 2020 lockdown. A powerful reason had brought that every school, college, and university, everything was closed. We were aware of a new way to serve our education at the time, known as "Online Class."
That online class has both positive and negative aspects. But what saddened or disappointed me was that many students did not 
respect their senior teachers simply because they were unfamiliar with computer/technology stuff, and as a result, our respected teachers made a few mistakes. Students mocked and trolled them, which was wrong. So I created this simple website with Ai/ML to assist our esteemed teachers. It is automated, 
so a teacher only needs to uploadhis or her recorded class; after that, my website will save the recorded video in the appropriate folder as 'subject' and also save it in text format with a summary of that class.
</p>

<h1>Methodology</h1>
<ul>
<li>
<h2>Data Collection</h2><br>
As my input format is recorded class, which is video format, I've decided to collect data from `YouTube` as there are free tutorial videos there.
I want to express my graditute to <b>CrashCourse</b>, <b>Art of Wei</b>, <b>Khan Academy</b>, <b>Professor Dave Explains</b>, <b>thenewboston</b>, <b>The School of Life</b> YouTube mentors for your amazing Tutorials made education easy for all and I used your data.
I collected videos based on different subjects. Subjects are <b>History</b>, <b>Art</b>, <b>Physics</b>,
<b>Chemistry</b>, <b>Biology</b>, <b>Astrology</b>, <b>Literature</b>, <b>Philosophy</b>, <b>Politics</b>,
<b>Economics</b>, <b>Phychology</b>, <b>Sociology</b>. <a href='https://github.com/AklimaRimi/Relax-Teacher/blob/main/scripts/download-vids.py'>Code here</a>
<br><br>I've downloaded 700 videos, which means my dataset size is 700. 
</li>
<li>
<h2>Data Preprocessing</h2><br>
This step was very important for this project. For the sake of this project, I need to convert <strong>Video</strong> to <strong>Audio</strong>, then strong>Audio</strong> to <strong>Text</strong>. And finally from the <b>Text</b> to <b>Summary</b>. I used this <b>Summay</b> for classification of the subject the uploaded video is teaching. <br><br>
  - For video to audio conversion, I used <strong>Moviepy</strong> Python library . <br><br>
  - To convert this audio to text, I used <strong>HuggingFace</strong> pretrained model. I tried several models, namely <b>openai/whisper-base.en, whisper-large, whisper-tiny</b> and I found <b>openai/whisper-base.en</b> more accurate. <a href ="https://github.com/AklimaRimi/Relax-Teacher/blob/main/scripts/audioToText.ipynb" > Code</a><br><br>
  - And lastly for text to summary again, I tried <b> HuggingFace</b> buit-in models  to compare the models and use the best one, models were <b>"facebook/bart-large-cnn","philschmid/bart-large-cnn-samsum", "google/pegasus-cnn_dailymail" , "sshleifer/distilbart-cnn-12-6"</b> . I found "sshleifer/distilbart-cnn-12-6" is very fast and finalized this model. <a href='https://github.com/AklimaRimi/Relax-Teacher/blob/main/notebook/text_augmentation.ipynb'>Code</a><br><br>   
 </li>
 
 <li>
 <h2>Model Trainning </h2>
Using <a href = "https://github.com/AklimaRimi/Relax-Teacher/blob/main/data/datawithSummary%20(1).csv">this dataset, </a>, I started training a model and evaluated using <b>Blurr.</b> <br> <b>Blurr: Blurr is a new technique for teaching a model using a dataset. The teaching method is combined by <b>HuggingFace</b> and <b>Fastai</b> which makes it faster to train a model and get impressive accuracy. <br><br>  For training, I used the built-in model from <a href = "https://huggingface.co/models?pipeline_tag=text-classification&sort=downloads">HuggingFace</a> I used two models <br> 1. distilroberta-base  and<br>  2. j-hartmann/emotion-english-distilroberta-base <br>  And different <b>Batch sizes</b> : 2, 4, 16, 32

 </li>
 
 <li>
 <h2> Final Model Selection</h2>
 
 Here is all trainning results:
 
 |  Model | Batch Size | Accuracy|
 |--------|------------|---------|
 |emotion-english-distilroberta-base| 2| 21%|
 |emotion-english-distilroberta-base| 4| 212%|
 |emotion-english-distilroberta-base| 16| 41%|
 |emotion-english-distilroberta-base| 32| 21%|
 |distilroberta-base| 2| 11%|
 |distilroberta-base| 4| 23%|
 |distilroberta-base| 16| 51%|
 |distilroberta-base| 32| 98%|
 
 So this is obvious that I kept <strong>distilroberta-base</strong> model further use <a href = "https://github.com/AklimaRimi/Relax-Teacher/blob/main/notebook/model_train_test.ipynb">Code</a>.
 
 </li>
 
 <li>
 <h2>Model Size Compression</h2>
 
 
 <p>
 Model size compression is one of the important tasks in ML. As we all want to build 
 something which costs low memmory size also faster and accurate. So <b>Onnx </b> is the best, option in my opinion.<br><br> Before using onnx my final model size was 314 MB, and after using onnx my model was compressed and 
 reduced in size to 78.7 MB which is almost 5 times smaller than the original model. <br>  <br>
 </p>
 </li>
 
 <li>
 <h3>Deployment</h2>
 
 This project is deployed in HuggingFace Platform. It's a great place for Data Scientist or ML Engineer like Heaven. <a href = "https://huggingface.co/spaces/Rimi98/Relax-Teacher"> You can use this deployed app from here</a><br><br>
 Here it's deployed look..<br>
 <image src = "https://github.com/AklimaRimi/Relax-Teacher/blob/main/images/hf.png" width = '1000' height = '500'>
 
 </li>
 
 <h2>Interface</h2>
 
I was thinking, I would make it free through a website. For making the website, I used the Flask Framework.
 I made a very simple UI nothing complex is in it. All of my work using flask and the huggingface API is <a href = 'https://github.com/AklimaRimi/Relax-Teacher/tree/main/flask'>here</a><br><br>
 You can use my <a href = "">website.</a><br><br>
 
 Here is demo images of my website..<br>
 <image src = "https://github.com/AklimaRimi/Relax-Teacher/blob/main/images/web1.png" width = '1000' height = '500'>
 <br><br>
 <image src = "https://github.com/AklimaRimi/Relax-Teacher/blob/main/images/web2.png" width = '1000' height = '500'>
 
 <br>
 
 <ol>
 <li>"Subject: Astrology", Here Astrology is ML generated. The video summary classified this video's summary as Astrology</li>
 <li>The text in "context" is automatically generated from video's voice.</li>
 <li>And lastly, the text in "Summary" automatically generated from "Context"</li>
 </ol>
 
 </ul>
<h1>Problem That I've Faced and Solution</h1>

While I was working on this project, I faced several problems. <br><br>
    1. Converting video to an audio file. At first, I used  `subprocess` to convert `mp4` to "wav." But this process is slow. Then I used `moviepy` library, which was far faster than `subprocess`.<br>    
    2. The next problem that I had faced was the conversion of audio to text. I directly used `Huggingface` model, which gave me the text but only 30 seconds of video. Finally, I used `Pipeline` from transformars. This process helped get full text in a video in a faster way. <br>    
    3. The next problem was that I tried to convert the full text into a summary. That gave me errors multiple times. After a while, I found a resource on Youtube, that I have to make `Chunks` using whole text. Then I can feed this to a model for Summary. `chunk` is make whole text to sub-text with 512 words. 
    
    
<h1>Conclusion</h1>

This project is made for our honorable senior teachers, who are the nation builders. Please show some respect towards them.

If you think this project needs some changes or you want to contribute, please pull a request.

Thanks.


  

