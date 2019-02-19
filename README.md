# ADF_studies
this is a 21 week plan to study Adversarial Attacks and Defences

>paper reviews, tf-tutorials, and final report on GAN in /doc directory  
>reproduced models (in python) are in /src directory



### weekly schedule:
<details open><summary>finished progress</summary>

* week 1  
scheduled: Feb. 1- 7            
    
    1. read basics:
    Are Adversarial Examples inevitable? https://openreview.net/pdf?id=r1lWUoA9FQ  
    Adversarial Examples: Attacks and Defenses for Deep Learning https://arxiv.org/pdf/1712.07107.pdf  
    Explaining and Harnessing Adversarial Examples https://arxiv.org/abs/1412.6572  
    Intriguing properties of neural networks  https://arxiv.org/abs/1312.6199  
    Towards Evaluating the Robustness of Neural Networks https://arxiv.org/abs/1608.04644  
    Towards Deep Learning Models Resistant to Adversarial Attacks https://arxiv.org/abs/1706.06083  
    2. follow tensorflow tutorials to learn tensorflow for future needs:  
    https://www.tensorflow.org/tutorials/  
    —> do learn and use ML part  

result: [paper review](doc/paper_review/week01.md), [tensorflow tutorial:learn and use ML](https://github.com/5loaves-2fish-12basckets/ADF_studies/tree/master/doc/tensorflow/1_Learn_and_use_ML)    
finish date: Feb.19 

---
</details>


* week 2  
scheduled: Feb. 8 - 14  

    1. follow references and citations of previous papers   
    2. write a review on these papers  

    3. follow tensorflow tutorials to learn tensorflow for future needs:  
    https://www.tensorflow.org/tutorials/  
    —> do Research and experiment part  

* week 3  
scheduled: Feb. 15 - 21  

    1. read  (investigate certified robustness and provable defense)
Certified Robustness to Adversarial Examples with Differential Privacy  
https://arxiv.org/pdf/1802.03471.pdf  
Towards Fast Computation of Certified Robustness for ReLU Networks  
https://arxiv.org/pdf/1804.09699.pdf  
Provable Defenses against Adversarial Examples via the Convex Outer Adversarial Polytope  
https://arxiv.org/pdf/1711.00851.pdf  
Certified Robustness to Adversarial Examples with Differential Privacy  
https://arxiv.org/pdf/1802.03471.pdf  

    2. understand code  
code for certified robustness for relu networks  
https://github.com/huanzhang12/CertifiedReLURobustness  

    3. follow tensorflow tutorials to learn tensorflow for future needs:  
https://www.tensorflow.org/tutorials/  
—> do ML at production scale part   

* week 4  
scheduled: Feb. 22 - 28  

    1. follow references and citations of previous papers   
    2. write a review on these papers  
    3. follow tensorflow tutorials to learn tensorflow for future needs:  
https://www.tensorflow.org/tutorials/  
—> do generative models  

* week 5  
scheduled: Mar. 1 - 7  
(investigate NIPS challange)  
    1. read   
Adversarial Attacks and Defences Competition  
https://arxiv.org/pdf/1804.00097.pdf  
Defense against Adversarial Attacks Using High-Level Representation Guided Denoiser  
https://arxiv.org/abs/1712.02976  
Mitigating Adversarial Effects Through Randomization  
https://arxiv.org/pdf/1711.01991.pdf  
(code https://github.com/cihangxie/NIPS2017_adv_challenge_defense)  
Boosting Adversarial Attacks with Momentum  
https://arxiv.org/pdf/1710.06081.pdf  
(code https://github.com/dongyp13/Non-Targeted-Adversarial-Attacks)  
Ensemble Adversarial Training: Attacks and Defenses  
https://arxiv.org/abs/1705.07204  
(code https://github.com/sangxia/nips-2017-adversarial)  

    2. follow tensorflow tutorials to learn tensorflow for future needs:  
https://www.tensorflow.org/tutorials/  
—> do images  

* week 6  
scheduled: Mar. 8 - 14  
    1. follow references and citations of previous papers   
    2. write a review on these papers  

    3. follow tensorflow tutorials to learn tensorflow for future needs:  
https://www.tensorflow.org/tutorials/  
—> do sequences 

* week 7  
scheduled: Mar. 15 - 21  
    1. read  
universal adversarial patch   
https://medium.com/deep-dimension/deep-learning-papers-review-universal-adversarial-patch-a5ad222a62d2  
https://arxiv.org/pdf/1712.09665.pdf  
decision based black box attack  
https://openreview.net/pdf?id=SyZI0GWCZ  
spacially transform adversarial examples https://openreview.net/pdf?id=HyydRMZC-  

    2. finalize previous reviews and finish writing review paper  

    3. follow tensorflow tutorials to learn tensorflow for future needs:  
https://www.tensorflow.org/tutorials/  
—> do Load data and data representation  

* week 8  
scheduled: Mar. 22 - 28  

    1. reproduce Boosting Adversarial Attacks with Momentum (in pytorch)  
  
* week 9  
scheduled: Mar. 29 - Apr. 4 (there is holiday)  
    1. reproduce certified robustness (in pytorch)  
test Boosting Adversarial Attacks with Momentum against certified robustness  

\<full review of adversarial attacks and simple reproductions>  
* week 10  
scheduled: Apr. 5 - 11  (prepare midterm)

* week 11  
scheduled: Apr. 12 - 18 (Midterm)  
「  
Goal:   
(following certified robustness)  
try to come up with best defence against state of the art adversarial attack on mnist dataset  

* week 12  
scheduled: Apr. 19 - 25  


* week 13  
scheduled: Apr. 26 - May 2  

  
* week 14  
scheduled: May 3 - 9   

* week 15  
scheduled: May 10 - 16  
* week 16  
scheduled: May 17 - 23  
* week 17  
scheduled: May 24 - 30  
* week 18  
scheduled: May 31 - Jun. 6  

」  

\<come up with new idea and execute>  
* week 19  
scheduled: Jun. 7 - 13  
finish ADF results, write report  
* week 20  
scheduled: Jun. 14 - 20 (final) 
* week 21  
scheduled: Jun. 21 - 28  

finish ADF results, write report  

if there is time  
try  
https://medium.com/syncedreview/ai-brush-new-gan-tool-paints-worlds-2544e4e29c11  

\<wrap up for conclution>  


(因為找不到Adversarial attack 發展過程完善的整理，因此從最新的論文開始實作，依序往回找參考文獻，在自己整理出發展過程）  
參考列表：    
https://www.robust-ml.org/defenses/    
https://github.com/IBM/adversarial-robustness-toolbox    

https://github.com/yenchenlin/awesome-adversarial-machine-learning    
https://medium.com/@wielandbr/reading-list-for-the-nips-2018-adversarial-vision-challenge-63cbac345b2f    
https://nicholas.carlini.com/writing/2018/adversarial-machine-learning-reading-list.html    

conference list    
https://aaai18adversarial.github.io/    
