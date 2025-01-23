import os

# 変更したい画像が保存されているフォルダのパス
folder_path = "data/val/dog"

# ファイル名の共通部分
new_name_base = "dog"
suffix = "val.png"

# ファイル拡張子のリスト
extensions = [".jpg", ".png", ".jpeg"]

# フォルダ内のファイルを一括でリネーム
def rename_images(folder_path, new_name_base, suffix, extensions):
    # フォルダ内のファイル一覧を取得
    files = os.listdir(folder_path)
    counter = 1  # ファイル名に付ける番号

    for file in files:
        # ファイルの拡張子を取得
        _, ext = os.path.splitext(file)
        
        # 対象の拡張子の場合のみ処理
        if ext.lower() in extensions:
            # `XX` をゼロ埋めした連番に変換
            serial_number = f"{counter:02d}"  # 例: 01, 02, 03...
            
            # 新しいファイル名を作成
            new_name = f"{new_name_base}_{serial_number}_{suffix}"
            
            # ファイルのパスを取得
            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(folder_path, new_name)
            
            # ファイル名を変更
            os.rename(old_path, new_path)
            print(f"Renamed: {file} -> {new_name}")
            
            # 番号をインクリメント
            counter += 1

# 関数を実行
if __name__ == "__main__":
    rename_images(folder_path, new_name_base, suffix, extensions)