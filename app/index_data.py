from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3
from app.extract_text import extract_text_from_pdf

host = 'search-rag-oswaldo-4haicg4dtm3jvmr65gtyi4rtey.us-east-1.es.amazonaws.com'
region = 'us-east-1'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

opensearch = OpenSearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

def index_pdf_data(file_path, title, author, date):
    text = extract_text_from_pdf(file_path)
    document = {
        'title': title,
        'content': text,
        'author': author,
        'date': date
    }
    response = opensearch.index(index="pdf-index", body=document)
    return response

# Example usage
if __name__ == "__main__":
    file_path = '/Users/ozzy/Documents/rag-chatbot/dinosaurs-data-test.pdf'  # Update this to your actual PDF file path
    title = 'Example PDF'
    author = 'John Doe'
    date = '2023-06-28'
    print(index_pdf_data(file_path, title, author, date))
