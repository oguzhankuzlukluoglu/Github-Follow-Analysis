
## API usage

#### First, clone the repository:

```http
  git clone https://github.com/oguzhankuzlukluoglu/Github-Follow-Analysis
```

| Parametre | Tip     | Açıklama                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Gerekli**. API anahtarınız. |

#### Install dependencies:

```http
 pip install requests
```
## Usage
python github_follow_analysis.py <github_username>


#### add(num1, num2)

Analyzing follow relationships for GitHub user 'your_username'...

--- SUMMARY ---
Total followers: 150
Total following: 120
Mutual follows: 100

--- USERS NOT FOLLOWING YOU BACK ---
- user1
- user2

--- USERS YOU DON'T FOLLOW BACK ---
- user3
- user4


  
