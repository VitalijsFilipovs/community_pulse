from app import create_app
from app.models.questions import Question
from app.models.response import Response


from flasgger import Swagger

app = create_app()
swagger = Swagger(app)

if __name__ == "__main__":
    app.run(debug=True)
