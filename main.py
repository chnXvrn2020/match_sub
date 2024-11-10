import os
import time


def file_list(path, ext):
    files = []

    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isfile(item_path):
            if ext == 'video':
                file_name, _ = os.path.splitext(item)
                files.append(file_name)
            elif ext == 'sub':
                files.append(item_path)

    return files

def input_path(msg):
    while True:
        path = input(f"{msg}이 있는 디렉토리를 전체 경로로 입력하세요.\n")
        if path != '':
            break
        print('아무것도 입력되지 않았습니다.')

    return path

def validate_files(video, sub):
    if len(video) == 0:
        print('비디오 폴더가 비어 있습니다.')
        return False
    if len(sub) == 0:
        print('자막 폴더가 비어 있습니다.')
        return False
    if len(video) != len(sub):
        print('비디오 파일과 자막 파일 갯수가 서로 상이합니다.')
        return False

    return True

if __name__ == '__main__':
    VIDEO_FILE_MSG = '비디오 파일'
    SUBTITLE_FILE_MSG = '자막 파일'

    print('+--------------------+')
    print('|비디오 자막 파일명 변환기|')
    print('+--------------------+')

    print('')

    print('설명 : 비디오 파일명을 기준으로 여러개의 자막 파일명을 자동으로 변환시켜 주는 프로그램입니다.')
    print('비디오 파일과 자막 파일은 별도의 디렉토리에 존재해야하며, 비디오 파일과 자막파일 갯수가 맞지 않으면 실행되지 않습니다.')
    print('제작 : verniy | email : breezeisland8@gmail.com')

    print('')

    while True:
        video_path = input_path(VIDEO_FILE_MSG)
        sub_path = input_path(SUBTITLE_FILE_MSG)

        video_files = file_list(video_path, 'video')
        sub_files = file_list(sub_path, 'sub')

        if validate_files(video_files, sub_files):
            break

    print('작업을 시작합니다.')

    for i, video in enumerate(video_files):
        _, ext = os.path.splitext(sub_files[i])
        new_name = f"{video}{ext}"
        new_path = os.path.join(sub_path, new_name)
        os.rename(sub_files[i], new_path)

    print('작업이 완료되었습니다. 즐거운 시간되십시오~!')

    time.sleep(5)
