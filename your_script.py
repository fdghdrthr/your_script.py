import pandas as pd

def generate_fake_data():
    fake_data = {
        'Email': ['fake1@example.com', 'fake2@example.com'],
        'Phone': ['123-456-7890', '987-654-3210'],
        # 添加其他列和数据
    }

    df = pd.DataFrame(fake_data)
    df.to_csv('input.csv', index=False)

def extract_information(input_csv_path, output_csv_path):
    # 读取CSV文件
    df = pd.read_csv(input_csv_path)

    # 提取信息
    # ...（您之前的提取信息代码）

    # 创建包含信息的新DataFrame
    result_df = pd.DataFrame(extracted_data)

    # 保存新的CSV文件
    result_df.to_csv(output_csv_path, index=False)

if __name__ == "__main__":
    generate_fake_data()  # 运行生成测试数据的函数
    extract_information('input.csv', 'output.csv')  # 运行您的提取信息脚本

import pandas as pd

def extract_information(input_csv_path, output_csv_path):
    # 读取CSV文件
    df = pd.read_csv(input_csv_path)

    # 提取信息
    extracted_data = {
        '电子邮箱': df['Email'],
        '电话': df['Phone'],
        'Skype': df['Skype'],
        'UID': df['UID'],
        '拥有者': df['Owner'],
        'Source': df['Source'],
        '关键词': df['Keywords'],
        '称谓': df['Title'],
        'Meta关键词': df['MetaKeywords'],
        'Meta描述': df['MetaDescription'],
        '域': df['Domain'],
        '街道地址': df['StreetAddress'],
        'Phone 2': df['Phone2'],
        'Category': df['Category']
    }

    # 创建包含提取信息的新DataFrame
    result_df = pd.DataFrame(extracted_data)

    # 保存新的CSV文件
    result_df.to_csv(output_csv_path, index=False)

# 示例用法
df.to_csv('C:\\Users\\Administrator\\Desktop\\input.csv', index=False) # 请替换为实际的输入文件路径
result_df.to_csv('C:\\Users\\Administrator\\Desktop\\output.csv', index=False)  # 请替换为实际的输出文件路径

extract_information(input_file_path, output_file_path)