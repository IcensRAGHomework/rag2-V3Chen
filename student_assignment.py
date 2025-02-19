from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"

def load_with_pyPdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs

def print_docs(docs):
    count = 0
    for doc in docs:
        print("--- Doc ", count, " begin ---")
        print("=== Page content ===")
        print(doc.page_content)
        print("====================")
        print("=== Metadata ===")
        print(doc.metadata)
        print("====================")
        print("--- Doc ", count, " end ---")
        count = count + 1

def split_text():
    split_target = "vi_n_ce t3_chen_f204-guilty-a08-zesponse_check!@update"
    spliter = CharacterTextSplitter(separator="_", chunk_size=7, chunk_overlap=0)
    result = spliter.split_text(split_target)
    print(result)

def split_doc():
    docs = [Document(page_content="iOS does not have a general-purpose API for Wi-Fi scanning and configuration."),
            Document(page_content="Howner, it does support a wide range of special-purpose Wi-Fi APIs."),
            Document(page_content="This technote lists some use cases supported by those special-purpose APIs.")]
    spliter = CharacterTextSplitter(separator="e", chunk_size=7, chunk_overlap=0)
    result = spliter.split_documents(docs)
    print(result)

def recursive_split_text():
    split_target = "ABC - DEF dfdfdf- GHI - JKL - MNO - PQR - STU - VW - XYZ"
    print("Before Split  :", split_target)

    spliter = RecursiveCharacterTextSplitter(separators=["-", " "],
                                             chunk_size=6,
                                             chunk_overlap=0)
    result = spliter.split_text(split_target)
    print("\"-\" ,\" \" split:", result)

def recursive_split_with_regex(input_pdf):
    loader = PyPDFLoader(input_pdf)
    docs = loader.load()
    text = ""
    for doc in docs:
        text = text + doc.page_content + "\n"
    spliter = RecursiveCharacterTextSplitter(separators=["第 (?:[一二三四五六七八九十]+|\\d+-?\\d*) (?:章|條\n)"], chunk_size=0, chunk_overlap=0, is_separator_regex=True, keep_separator=True)
    result = spliter.create_documents([text])
    print(len(result))
    # print(result)
    # print_docs(result)
    # print(result[0])
    # print(result[1])
    # print(result[2])
    # print(result[3])
    # print(result[4])
    return len(result)


# split_doc()
# print_docs(load_with_pyPdf(q1_pdf))
# recursive_split_text()
recursive_split_with_regex(q2_pdf)
print("wahaha")

def hw02_1(q1_pdf):
    q1_doc = load_with_pyPdf(q1_pdf)
    q1_spliter = CharacterTextSplitter(separator=" ", chunk_size=5, chunk_overlap=0)
    result = q1_spliter.split_documents(q1_doc)
    print(result[-1])
    return result[-1]

def hw02_2(q2_pdf):
    recursive_split_with_regex(q2_pdf)
    pass
