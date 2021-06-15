import boto3

s3 = boto3.client('s3')
transcribe = boto3.client('transcribe')

def lambda_handler(event, context):
    for record in event['Records']:
        file_bucket = record['s3']['bucket']['name']
        file_name = record['s3']['object']['key']
        object_url = 'https://s3.amazonaws.com/{1}/{2}'.format(
            file_bucket, file_name)

        response = transcribe.start_transcription_job(
            TranscriptionJobName=file_name.replace('/', '')[:10],
            LanguageCode='es-US',
            MediaFormat='mp3',
            Media={
                'MediaFileUri': object_url
            })
        
        print(response)