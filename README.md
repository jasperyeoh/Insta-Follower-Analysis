# 📊 Instagram Follower/Following Analysis Toolkit  
## 简介 (Introduction)  
这是一个简单的 Python 工具集，用于分析 Instagram 帐号的 Follower 和 Following 数据。通过这些脚本，你可以轻松：  
- 找出未回关你的用户。  
- 分析谁在不同时间段内取关了你。  

This is a simple Python toolkit for analyzing the follower and following data of Instagram accounts. With these scripts, you can:  
- Identify users who haven't followed you back.  
- Analyze who unfollowed you over time.  

---

## 🛠 功能 (Features)  
1. **提取用户名**：从 Instagram 的 HTML 数据文件中提取 Follower 和 Following 用户名列表。(从个人信息中下载，选择下载所有时间的followers and following data)
2. **未回关用户分析**：对比 Follower 和 Following，找出未回关你的用户。  
3. **历史数据对比**：比较之前的记录，找出新增的未回关用户。  
4. **取关分析**：通过不同时间段的 Follower 快照，识别取关用户。  

1. **Extract Usernames**: Extract follower and following username lists from Instagram HTML data files. (Download your personal information from instagram, then click "follower and following", select all)
2. **Non-Followback Detection**: Compare followers and followings to find users who don’t follow you back.  
3. **Historical Comparison**: Compare previous records to find newly added non-followback users.  
4. **Unfollow Analysis**: Detect users who unfollowed you by comparing snapshots of follower data.  

---

## 🚀 快速开始 (Quick Start)  

### 1. 提取用户名 (Extract Usernames)  
运行 `1_filtering.py`，从 Instagram 的 HTML 文件中提取并保存用户名：  
Run `1_filtering.py` to extract and save usernames from Instagram HTML files:  
```bash
python 1_filtering.py

输出文件 (Output files)：
	•	extracted_followers_usernames.txt：提取的 Follower 用户名。
	•	extracted_following_usernames.txt：提取的 Following 用户名。

2. 找出未回关用户 (Find Non-Followers)

运行 2_compare.py，找出未回关你的用户：
Run 2_compare.py to identify users who haven’t followed you back:

python 2_compare.py

输出文件 (Output file)：
	•	not_following_back.txt：未回关你的用户名列表。

3. 历史数据对比 (Compare Historical Data)

运行 3_compare_previous.py，对比之前的未回关数据：
Run 3_compare_previous.py to compare historical non-followback data:

python 3_compare_previous.py

输出文件 (Output file)：
	•	not_in_base.txt：新增的未回关用户名列表。

4. 取关分析 (Unfollow Analysis)

运行 4_follower_loss.py，分析取关你的用户：
Run 4_follower_loss.py to analyze users who unfollowed you:

python 4_follower_loss.py

输出文件 (Output file)：
	•	follower_loss_1.txt：取关用户名列表。

💡 依赖 (Dependencies)
	•	Python 3.x
	•	BeautifulSoup4

安装依赖 (Install dependencies)：

pip install beautifulsoup4


如果你有任何问题或建议，请随时联系！
Feel free to reach out if you have any questions or suggestions! 😊
