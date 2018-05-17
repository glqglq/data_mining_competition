# glq

- browse_count_7_division：过去所有的天平均浏览量
- buy_count_7_division：过去所有的天平均转化量
- 【有效】ratio_7：转化率
- browse_count_hour_ago_3600：过去一小时内浏览量
- browse_count_hour_ago_1800：过去30分钟内浏览量
- browse_count_hour_ago_900：过去15分钟内浏览量
- browse_count_today：今天的浏览量（leak）
- browse_count_tohour：这个小时的浏览量（leak）
- day_browse_is_last：今天是否最后一次浏览（leak）
- hour_browse_is_last：本小时是否第一次浏览（leak）
- 【有效】property-jaccard：jaccard相似度
- **【无效】embedding-similarity：embedding相似度**
- **【无效】proportion：展示、收藏、销量之间的比例**
- **【部分有效】last_browse_time_interval：上次浏览距离本次浏览的时间差**
- **【有效】next_browse_time_interval：下次浏览距离本次浏览的时间差**

# 浩彬师兄

- user item交叉特征（前1/2/4个半小时的点击购买数，后1/2/4个半小时的点击数） 9维
- item/shop/user （前1/2/4个半小时的点击购买数，后1/2/4个半小时的点击数） 27维
- userid 距离上次/下次点击的时间间隔 2维
- 【待定】我做的一些简单统计特征（就是师弟标 浩彬 的那批特征）
  - 包括商铺中shop item sale min，shop item price min，shop user age mean，shop category count。类别中cat item count，

# 冲哥

- clickTradeRatioFeat：点击占比，感觉需要把 user_id相关的删除
- userDayClickRankFeat：当天点击排序
- preDayClickCountFeat：前一天的点击量
- shiftDayItemClickCountFeat：偏移过的前一天的点击量
- shiftDayShopClickCountFeat：偏移过的前一天的点击量
- shopFeat：shop各种score的离散化
- singleCvrFeat：单特征转化率
- timeFeat：时间戳的变化，先不用管