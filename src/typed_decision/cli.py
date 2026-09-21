import laya_mlx as laya

def main():
    agent = laya.load("aac6fef/laya-multilingual-mlx")
    result = agent.predict(
        "发票被重复扣款，请退款。",
        {
            "department": {
                "type": "choice",
                "instructions": "Who should handle this?",
                "criteria": ["billing", "technical", "sales"],
            }
        },
    )
    print(result["answers"]["department"])
