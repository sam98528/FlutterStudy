import os
from collections import defaultdict


def list_md_files(directory, output_file):
    # 모든 .md 파일을 저장할 딕셔너리 (알파벳으로 분류)
    md_files_by_letter = defaultdict(list)
    total_files = 0

    # os.walk를 사용하여 디렉토리 내의 모든 파일을 탐색
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                # .md 파일의 이름에서 확장자를 제거
                file_name = os.path.splitext(file)[0]

                # 파일의 첫 글자를 기준으로 분류
                first_letter = file_name[0].upper()
                md_files_by_letter[first_letter].append(file_name)
                total_files += 1

                # 파일 경로 생성
                file_path = os.path.join(root, file)

                # 파일에 제목 줄이 있는지 확인하고 추가
                add_title_line_if_missing(file_path, file_name)

    # 결과를 정리하여 파일에 저장
    with open(output_file, "w", encoding="utf-8") as f:
        # 총 파일 개수를 파일 맨 위에 추가
        f.write(f"### Total Markdown Files: {total_files} ###\n\n")

        if md_files_by_letter:
            for letter in sorted(md_files_by_letter):
                f.write(f"# {letter}\n")
                for file in sorted(md_files_by_letter[letter]):
                    f.write(f"[[{file}]]\n")
                f.write("\n")  # 알파벳 그룹 사이에 빈 줄 추가
        else:
            f.write("No markdown files found in the directory.\n")


def add_title_line_if_missing(file_path, file_name):
    with open(file_path, "r+", encoding="utf-8") as f:
        lines = f.readlines()

        # 첫 줄에 제목 형식이 없으면 추가
        if not lines or not lines[0].strip() == f"## {file_name} ##":
            # 파일의 시작 부분에 제목 줄 추가
            f.seek(0, 0)
            f.write(f"## {file_name} ##\n" + "".join(lines))


if __name__ == "__main__":
    # /Flutter 폴더의 경로
    flutter_directory = "./Flutter"
    # 결과를 저장할 파일 이름
    output_file = "Flutter Keyword.md"
    list_md_files(flutter_directory, output_file)
