# gcp-svc-sample

Cloud RunからVPC内のGCEにリクエストを送信するデモ

## 前準備
- VPC, サーバレスVPCアクセスを構成
- internalを任意のコンテナレジストリに上げておく

## internal
docker on GCEで実行

```
docker pull [image name]
docker run -d -p 80:8080 -e PORT=8080 [image ID]
```

## external
Cloud Runで実行

```
cd external
gcloud run deploy
```
