# music-xml-20880108
HCMUS - ĐTTX - Chuyên đề TCDL - BT4


## Bài luận tìm hiểu MusicXML

### MusicXML là gì?

MusicXML là định dạng tệp tin dựa trên XML để biểu diễn ký hiệu nhạc tây phương. Định dạng này là mở, được tài liệu hoàn chỉnh và có thể được sử dụng miễn phí dưới Sự đồng thuận về Đặc tả Cuối cùng của Cộng đồng W3C. MusicXML được sử dụng để lưu trữ và chia sẻ thông tin về bản nhạc, bao gồm các ghi chú, hợp âm, nốt nhạc, nhịp điệu, ký hiệu và các thông tin khác về kết cấu và nội dung của bản nhạc. Nó được thiết kế để có thể đọc được bởi các chương trình ghi nhạc hoặc phần mềm chỉnh sửa âm nhạc và cho phép người dùng dễ dàng chuyển đổi, chỉnh sửa và chia sẻ bản nhạc của họ trên nhiều nền tảng khác nhau.

### Một số công cụ hỗ trợ mã nguồn mở

1. MuseScore: Một phần mềm ghi nhạc mã nguồn mở và miễn phí hỗ trợ nhập, chỉnh sửa và xuất file MusicXML.

2. LilyPond: Một phần mềm ghi nhạc mã nguồn mở và miễn phí hỗ trợ nhập file MusicXML và cũng có thể xuất file dưới định dạng MusicXML.

3. Verovio: Một toolkit mã nguồn mở dùng để biểu diễn file MusicXML dưới dạng sheet music trong các ứng dụng trên web, thiết bị di động và máy tính.

4. Music21: Một thư viện Python mã nguồn mở dùng để làm việc với dữ liệu âm nhạc, bao gồm cả file MusicXML.
EasyABC: Một phần mềm ghi nhạc miễn phí hỗ trợ nhập và xuất file MusicXML, cũng như các định dạng khác như ABC.

### Một số tập tin ví dụ MusicXML từ bản nhạc đơn giản:

Jingle bells: https://github.com/ductruong253/music-xml-20880108/blob/master/jingle_bells.xml

### Chương trình Python xử lý tập tin MusicXML với các thao tác:

- Thay đổi tốc độ (tempo)
- Thay đổi giọng (transpose)
- Thay đổi cường độ (dynamic)
- Thêm bè đệm với các hợp âm (chord) và tiết điệu (rhythm) đơn giản

Vui lòng tham khảo file tại: https://github.com/ductruong253/music-xml-20880108/blob/master/musicXml_processor.py

### Hướng dẫn sử dụng:

Các phần mềm cần thiết:

`python3, pip`

Cài đặt music21 bằng cách chạy lệnh trong terminal/command promt

`pip install music21`

Đặt tập tin musicXML cần xử lý vào cùng thư mục với file “musicXml_processor.py”

Mở file “musicXml_processor.py”, sửa dòng 32 thành

`processor = MusicXMLProcessor('<tên file cần xử lý>.xml')`

Sửa tên file sau khi xử lý tại dòng 37

`processor.save('<tên file sau khi xử lý>.xml')`

Lưu lại và vào terminal/command promt, trỏ đến thư mục chứa file “musicXml_processor.py”

Chạy lệnh: `python3  musicXml_processor.py`

Kết quả sẽ tạo ra 1 file kết quả nằm cùng thư mục