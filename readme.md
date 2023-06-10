# I. Giới thiệu về project
- Chào mừng bạn đến với project của mình về **Chess Women Players**. Trong phần trình bày này, mình sẽ thảo luận về kết quả *phân tích dữ liệu khám phá (EDA)* của tôi trên bộ dữ liệu về các trò chơi cờ vua do kì thủ nữ chơi.
- Ngoài ra thì mình còn làm thêm phần cắt **Frame** và **Game**
- Mình là Lê Thành Vinh (**21110940**). Đây là project cho đồ án môn **Lập trình Python** của mình. Mình sẽ trình bày về project của mình qua các phần sau:
  - Phần I: Giới thiệu về project
  - Phần II: Các form (GUI) chính của project
  - Phần III: Kết luận

# II. Các form (GUI) chính của project
## 1. Form chính (Form Main):
![Alt text](G3_84_LeThanhVinh_ChessWomen/main1.png?raw=true "Title")
> Form chính này được tạo từ thư viện **customTkinter**. Các phần được chia theo kiểu *tabview*. Mỗi form sẽ nằm trong từng tab của tabview. Ở hình trên, tab đầu tiên là về phần giới thiệu
> 
![Alt text](G3_84_LeThanhVinh_ChessWomen/main2.png?raw=true "Title")
> Đây là tab phần EDA. Nếu nhấn nút Button thì sẽ mở form EDA
>
![Alt text](G3_84_LeThanhVinh_ChessWomen/main3.png?raw=true "Title")
> Đây là tab phần cắt Frame. Nếu nhấn nút Button thì sẽ mở form Frame
>
![Alt text](G3_84_LeThanhVinh_ChessWomen/main4.png?raw=true "Title")
> Đây là tab phần cắt Game. Nếu nhấn nút Button thì sẽ mở form Game
>
## 2. Form EDA:
![Alt text](G3_84_LeThanhVinh_ChessWomen/EDAMain.png?raw=true "Title")
> Các chức năng liên quan đến *EDA*:
> 
  Có các nút để mở các chức năng như **mở file**, **xử lí cột null**, **xử lí dòng null**, **z-core**, **chuẩn hóa**.
> Các chức năng liên quan đến *Vẽ đồ thị*:
> 
  Có các nút để mở các đồ thị: **bar charts**, **pie charts**, **scatter plots**, và **3D scatter plots**
> Các chức năng liên quan đến *Xử lí giọng nói*:
> 
  Khi cần nhập liệu bằng giọng nói, người dùng sẽ nói bằng các số. Bảng tra giữa các số và chức năng được ghi trên label bên cạnh. Sau khi người dùng nói thì kết quả sẽ được hiện trên label. Cuối cùng chỉ cần nhấn nút **Xác nhận** thì lệnh sẽ được thực hiện
## 3. Form Frame:
![Alt text](G3_84_LeThanhVinh_ChessWomen/FrameMain.png?raw=true "Title")
> Các chức năng liên quan đến *Frame*:
>
- **OpenFile**: Cho phép người dùng chọn tệp video.
- **OpenFolder**: Cho phép người dùng chọn thư mục để lưu khung hình.
- **SaveFrames**: Lưu tất cả các khung hình từ video vào thư mục đã chọn.
- **StartCut**: Cho phép người dùng chọn thời gian bắt đầu cắt khung.
- **EndCut**: Cho phép người dùng lựa chọn thời gian kết thúc cắt khung.
- **SaveFramesCut**: Lưu khung hình giữa thời gian bắt đầu và kết thúc đã chọn vào thư mục đã chọn.
- **FlipVertical**: Lật khung hình theo chiều dọc.
- **AddColor**: Thêm màu cho khung hình.
- **GUI**: Khởi tạo GUI và khởi động chương trình.
  
## 4. Form Game:
![Alt text](G3_84_LeThanhVinh_ChessWomen/GameMain.png?raw=true "Title")

# III. Kết luận

- Trong project này, mình đã thực hiện được các chức năng cơ bản như:
  - Phân tích dữ liệu khám phá (EDA)
  - Cắt Frame
  - Cắt Game

- Mình đã học được rất nhiều từ project này. Mình đã học được cách sử dụng các thư viện như 
  - **Speech**: speech_recognition, gtts, playsound, re
  - **GUI**:  tkinter, customtkinter, os
  - **EDA**:  pandas, numpy, scipy, sklearn, PIL, seaborn, matplotlib
  - **Frame**:  cv2, time
  - **Game**:  cv2, pygame, sys, random
- Cảm ơn các bạn đã xem project của mình

![Thanks GIF](G3_84_LeThanhVinh_ChessWomen/touhou-youmu.gif?raw=true "Title")
