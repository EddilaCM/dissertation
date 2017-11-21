personal message before the graducation of my Master

# dataset introduction

TMALL is an important business unit of Alibaba Group. As the top one B2C platform in China. "REC-TMALL" is a set of RECommendation-related data provided by TMALL.

Tianchi_2014001_Rec_Tmall_Product
It contains 8133507rows, which correspond to the attributes of 8133507 items on TMALL. In each row, there are 4 features listed as following.


Column
               	Description

Item_id 	An integer in[1, 8133507]£¬denoting an unique item (Remark: A product simultaneously offered by more than two merchants is recorded in multiple rows with different IDs. E.g., popular cellphones as iPhone 6.).

Title 	A string containing multiple key words, separated by ' '  . There words are extracted from the raw title by an NLP system.

Pict_url 	An URL linked to corresponding image online.

Category
 	A string as "x-y"£¬where ' x' denotes its parent category while ' y' represents its leave category.
Brand_id 	A string as "b1", "b89366", denoting the brand of the item.
Seller_id 	A string as "s1", "s86799", denoting the seller who sells the item.

Typical research topics
The prediction of popularity of item from its attributes.


Tianchi_2014002_Rec_Tmall_Log
The users¡¯ behavior of browsing TMALL reflects their preference of items. This data set contains 25432915908 rows corresponding to records of user-item interactions. Features of each row are listed as below.


Column
 	Description

Item_id 	An integer in[1, 8133507], denoting an unique item

 User_id	A string as "u9774184", denoting an unique user.

Action 	Type of behavior, a string like "click", "collect", "cart", "alipay", represents for ' click' , ' add to favorite' , ' add to cart' and ' purchase' , respectively.

Vtime
 	Timestamp  of then behavior, a string as "yyyy-mm-dd hh:mm:ss".

Typical research topics
a) Matrix completion
b) Ranking

Tianchi_2014003_Rec_Tmall_Review
Review data is available for partial "user-item" pairs, which contains the review and rating on the item/merchant/logistic. This data set contains 241919749 rows, corresponding to 241919749 reviews.£¨Remark£ºA user may buy the same item for multiple time, thus there may be several reviews for a "user-item" pair. Also, a review with ' n' images will be decomposed into ' n' identical reviews except feature ' image' . Features are listed as below.


Column
 	Description

Item_id 	An integer in[1, 8133507], denoting an unique item

 User_id	A string as "u9774184", denoting an unique user.

feedback 	A string containing multiple key words, separated by ' '  . There words are extracted from the raw title by an NLP system.

rate_pic_url
 	An URL linked to corresponding image online. One may use the provided script "download" to download all images as a batch.
Gmt_create 	Timestamp of the review, A string as "yyyy-mm-dd hh:mm:ss".




Typical research topics
a) Rating
b) Transfer Learning

Reference and Related Publichations
a) Yuyu Zhang, Liang Pang, Lei Shi, Bin Wang,"Large Scale Purchase Prediction with Historical User Actions on B2C Online Retail Platform", Accepted by 2nd Large Scale Recommender Systems Workshop, RecSys 2014
b) W. Zhong, R. Jin, et. al., "Stock Constrained Recommendation in Tmall", In Proceedings of  the 21th ACM SIGKDD international conference on Knowledge discovery and data mining, ACM, 2015

