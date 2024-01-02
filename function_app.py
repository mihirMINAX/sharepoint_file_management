import requests
import os


def auth():
    url = "https://login.microsoftonline.com/9c62dec9-2bdd-4bc3-bff3-9eab2927b956/oauth2/v2.0/token"

    payload = {
        "grant_type": "client_credentials",
        "client_id": "41128a0d-ef89-4587-9350-d3a25a046561",
        "client_secret": "QNk8Q~AN73zfCo2xwGzPDbPN5ksGEv4nfrFf-cVl",
        "scope": "https://graph.microsoft.com/.default",
    }
    headers = {}

    response = requests.post(url, headers=headers, data=payload).json()

    if "access_token" in response:
        access_token = response["access_token"]
        return access_token
    else:
        print("Authentication failed")
        return None


def uploadFile(content, access_token):
    url = "https://graph.microsoft.com/v1.0/sites/ea8c8959-fe76-418f-8d8f-452f8f44a832/drives/b!WYmM6nb-j0GNj0Uvj0SoMm6oLAN4yXNKq1rZC0nFJWd8FGEJPFYGS6m7WZTsDhrN/root:/HTML-PDF/uo_3.html:/content"

    headers = {
        "Authorization": access_token,
        "Content-Type": "text/html",
    }

    response = requests.request("PUT", url, headers=headers, data=content)

    print("file Uploaded", response.status_code)


def filehandling():
    try:
        access_token = auth()
        if access_token:
            # site_url = (
            #     "https://graph.microsoft.com/v1.0/sites?search=TestingPurposeOnly"
            # )
            access_token = "Bearer " + access_token

            headers = {"Authorization": access_token}
            # response = requests.request("GET", site_url, headers=headers).json()

            site_id = "ea8c8959-fe76-418f-8d8f-452f8f44a832"
            folder_id = (
                "b!WYmM6nb-j0GNj0Uvj0SoMm6oLAN4yXNKq1rZC0nFJWd8FGEJPFYGS6m7WZTsDhrN"
            )
            file_id = "01R5HTJHZJYEM4I2OC2RAYNR4JKLJS2TSD"
            graph_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{folder_id}/items/{file_id}/content"

            api = requests.request("POST", graph_url, headers=headers)
            content = api.content
            uploadFile(content, access_token)
            filename = "uo.html"
            # count = 1
            # while os.path.exists(filename):
            #     filename, file_extension = os.path.splitext("uo.html")
            #     filename = f"{filename}_{count}{file_extension}"
            #     count += 1

            # with open(filename, "wb") as f:
            #     f.write(content)
            print(f"New file with Name {filename} Sucessfully Downloaded.")
        else:
            print("Authentication failed")
    except Exception as e:
        print(f"An error occurred: {e}")


filehandling()
