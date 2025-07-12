import json
import re
from typing import List, Dict

SPECIAL_TOKENS = ["<PAD>", "<START>", "<END>", "<UNK>"]

def json_to_tokens(data: Dict) -> List[str]:
    tokens = ["<START>"]
    tokens += ["<shop>", data["shop"], "</shop>"]
    tokens += ["<date>", data["date"], "</date>"]
    tokens += ["<total>", str(data["total"]), "</total>"]

    for item in data.get("items", []):
        tokens.append("<item>")
        tokens += ["<name>", item["name"], "</name>"]
        tokens += ["<qty>", str(item["qty"]), "</qty>"]
        tokens += ["<price>", str(item["price"]), "</price>"]
        tokens.append("</item>")

    tokens.append("<END>")
    return tokens

def build_vocab(token_lists: List[List[str]]) -> Dict[str, int]:
    vocab = {tok: i for i, tok in enumerate(SPECIAL_TOKENS)}
    idx = len(vocab)
    for tokens in token_lists:
        for t in tokens:
            if t not in vocab:
                vocab[t] = idx
                idx += 1
    return vocab

def tokens_to_ids(tokens: List[str], vocab: Dict[str, int]) -> List[int]:
    return [vocab.get(t, vocab["<UNK>"]) for t in tokens]

def ids_to_tokens(ids: List[int], inv_vocab: Dict[int, str]) -> List[str]:
    return [inv_vocab.get(i, "<UNK>") for i in ids]

def save_vocab(vocab: Dict[str, int], path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(vocab, f, indent=2)

def load_vocab(path: str) -> Dict[str, int]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
