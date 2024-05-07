import requests
import iam_token_generation
import info.creds


def speech_to_text(data):
    # iam_token, folder_id для доступа к Yandex SpeechKit
    iam_token = info.creds.iam_token
    folder_id = info.creds.folder_id

    params = "&".join([
        "topic=general",
        f"folderId={folder_id}",
        "lang=ru-RU"
    ])

    headers = {
        'Authorization': f'Bearer {iam_token}',
    }


    response = requests.post(
        f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{params}",
        headers=headers,
        data=data
    )

    # Читаем json в словарь
    decoded_data = response.json()
    # Проверяем, не произошла ли ошибка при запросе
    if decoded_data.get("error_code") is None:
        a =f"Текст аудио: {decoded_data.get("result")}"
        return a
    else:
        a = "При запросе в SpeechKit возникла ошибка"
        return a
