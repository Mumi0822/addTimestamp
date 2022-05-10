# addTimestamp  
**注意：このスクリプトは学生が練習用に書いたスクリプトですので私の使用環境で問題ない程度の最低限の例外処理やテストを施していませんのでお気を付けください。何かあっても保証できません**  
  
Ver1.0 2022/05/10　  
VRChatフォルダの写真をJPEG化してExifで撮影日時を自動でつけます。  
  
change_lib.py :基本機能   
     PtoJ(input_path,output_dir):input_pathで指定したPNGファイルのコピーをJPEGファイルとしてoutput_dirに生成　**注意：input_pathにPNG以外を指定した場合を考えずに作ってた。元ファイルに危険はないはず**  
     GetDT(basename) : VRC標準のスクリーンショットのファイル名から撮影日時をdatetimeで返す  
     AddExif(input_path) : GetDTで得たdatetimeをinput_pathにExif情報としてタグ付け  
     changefunc(in_path,out_dir) : in_pathの画像ファイルをPtoJ()とAddExif()に通してタグ付けしてout_dirに日付付きJPEGコピーが生成  
Exec_1.py : このスクリプトと同階層にあるVRChat/内の全ての画像を同じ階層のVRChat_JPEG/にJPEGコピーして撮影日時を付与  
(今までのpng画像を一括変換する用途を想定)  
Exec_2.py : VRChat/下の今月分のフォルダ内だけをVRChat_JPEG/にJPEGコピー  
(VRChat終了後に毎回自動で走るようにしておくと最新分だけを追加できる(重複は上書きされる))  
(明らかに冗長ですので今後仕様変更する予定)  
