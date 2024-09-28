import json
import pandas as pd

# Load the output Excel file
df_output = pd.read_excel('output_data.xlsx')

# Initialize empty lists for questions and answers
questions = []
answers = []

# Iterate through each row in the DataFrame
for index, row in df_output.iterrows():
    # Assuming 'assistant_response' column contains JSON data
    json_string = row['assistant_response']
    # Attempt to parse the JSON string
    try:
        parsed_data = json.loads(json_string)  # Check if json_string is valid
    except json.JSONDecodeError:
        print(f"Error decoding JSON in row {index}: {json_string}")
        continue
    
    # Access 'Question' and 'Answer' directly from parsed_data
    # Assuming parsed_data is a list of dictionaries with 'Question' and 'Answer' keys
    for item in parsed_data:
        questions.append(item['Question'])  # Corrected line
        answers.append(item['Answer'])      # Corrected line

# Create a list of question-answer pairs
qa_pairs = [{"Question": question, "Answer": answer} for question, answer in zip(questions, answers)]

# Display the question-answer pairs
for pair in qa_pairs:
    print(f"Question: {pair['Question']}\nAnswer: {pair['Answer']}\n")
    
# Save the results to a new Excel file
df_qa_pairs = pd.DataFrame(qa_pairs)
df_qa_pairs.to_excel('processed_data.xlsx', index=False)

# Data trong từng cột sẽ như sau: 

# [{"Question": "Chunking là gì và nó có vai trò như thế nào trong việc học tập?", "Answer": "Chunking là một phương pháp tổ chức thông tin thành các khối nhỏ hơn, giúp người học dễ dàng ghi nhớ và xử lý thông tin. Vai trò của chunking trong việc học tập là giúp người học giảm tải thông tin, từ đó cải thiện khả năng ghi nhớ và giảm thiểu tình trạng quên."}, {"Question": "Drilling là gì và tại sao nó lại quan trọng trong quá trình học?", "Answer": "Drilling là một phương pháp luyện tập lặp đi lặp lại nhằm củng cố kiến thức và kỹ năng. Nó quan trọng trong quá trình học vì giúp người học ghi nhớ thông tin lâu hơn và tăng cường khả năng sử dụng kiến thức trong thực tế."}, {"Question": "Tại sao việc kết hợp chunking và drilling lại được coi là giải pháp hiệu quả cho vấn đề học rồi quên?", "Answer": "Việc kết hợp chunking và drilling tạo ra một phương pháp học tập toàn diện, trong đó chunking giúp tổ chức thông tin một cách hợp lý, còn drilling giúp củng cố và lặp lại thông tin đó. Sự kết hợp này giúp người học không chỉ ghi nhớ thông tin mà còn sử dụng chúng một cách hiệu quả."}, {"Question": "Có những lợi ích gì khi áp dụng phương pháp chunking trong học tập?", "Answer": "Lợi ích của phương pháp chunking bao gồm: giảm bớt khối lượng thông tin cần ghi nhớ, tăng cường khả năng ghi nhớ thông tin, giúp người học dễ dàng nhận diện và liên kết các khối thông tin với nhau, từ đó cải thiện hiệu quả học tập."}, {"Question": "Người học có thể áp dụng chunking và drilling như thế nào trong việc học của mình?", "Answer": "Người học có thể áp dụng chunking bằng cách chia nhỏ thông tin thành các phần dễ nhớ, ví dụ như nhóm các khái niệm liên quan lại với nhau. Sau đó, họ có thể sử dụng drilling bằng cách lặp lại các khối thông tin này qua các bài tập, câu hỏi ôn tập hoặc thảo luận nhóm để củng cố kiến thức."}]
# # [
#     {"Question": "Công dụng của tính năng Chunking là gì?", "Answer": "Tính năng Chunking cho phép người dùng xử lý và tạo ra các câu một cách nhanh chóng mà không cần phải suy nghĩ về từng từ."},
#     {"Question": "Lợi ích của việc sử dụng các mẫu câu đã được khắc sâu vào trí nhớ là gì?", "Answer": "Lợi ích của việc này là người dùng có thể nói lưu loát và tự tin hơn trong giao tiếp, vì họ không cần phải lo lắng về việc tìm từ trong lúc nói."},
#     {"Question": "Vấn đề mà người dùng thường gặp phải trong các cuộc trò chuyện là gì?", "Answer": "Người dùng thường quên những gì cần nói và gặp khó khăn trong việc ghép các từ lại với nhau trong các cuộc trò chuyện."},
#     {"Question": "Giải pháp nào được đề xuất để khắc phục vấn đề quên từ trong giao tiếp?", "Answer": "Giải pháp được đề xuất là sử dụng tính năng Chunking, cung cấp các cụm ngôn ngữ được lắp ráp sẵn đ��� người dùng có thể sử dụng trong các tình huống hội thoại khác nhau."},
#     {"Question": "Lợi ích của việc sử dụng tính năng Chunking là gì?", "Answer": "Lợi ích của việc sử dụng tính năng Chunking là người dùng có thể phản ứng nhanh chóng và chính xác trong giao tiếp mà không cần phải suy nghĩ về từng từ, từ đó giảm bớt lo lắng và tăng cường sự tự tin."},
#     {"Question": "Người dùng gặp phải vấn đề gì khi nói, mặc dù họ hiểu từ khi đọc hoặc nghe?", "Answer": "Người dùng gặp phải vấn đề là họ hiểu các từ khi đọc hoặc nghe, nhưng khi đến lúc nói, họ không thể thốt ra được từ nào."},
#     {"Question": "Giải pháp nào được đưa ra để giải quyết vấn đề không thể nói ra từ khi cần?", "Answer": "Giải pháp được đưa ra là The Coach, thông qua cơ chế Luyện Tập Chủ Động, kết hợp kỹ thuật Chunking với các bài tập nói có mục tiêu."},
#     {"Question": "Cơ chế Luyện Tập Chủ Động giúp ích như thế nào trong việc cải thiện khả năng nói?", "Answer": "Cơ chế Luyện Tập Chủ Động giúp cải thiện khả năng nói bằng cách kết hợp kỹ thuật Chunking với các bài tập nói có mục tiêu, giúp người dùng luyện tập và củng cố khả năng giao tiếp."}
# ]

### Hướng 1: Ban đầu copy tất cả các cột -> định xử lý JSON bằng ctrl H thay thế, ... KO ĐƯỢC  => thử chuyển qua code: ko được
### Hướng 2: Xử lý từng ô bằng code, xài crusor code quá nhanh - 5 min. 
### Hướng 3: Xài LLM quét qua: => 2 bước LLM nên gọi là: Chain of Prompt cũng được nhỉ. 
