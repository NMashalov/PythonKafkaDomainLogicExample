from app.domain.serializer.base import BaseSerializer
from app.domain.models.score import Score
from pydantic2avro import PydanticToAvroSchemaMaker
from io import BytesIO
from fastavro import parse_schema, writer


class ScoreSerializer(BaseSerializer[Score]):
    AVRO_SCHEMA = parse_schema(PydanticToAvroSchemaMaker(PydanticToAvroSchemaMaker).get_schema())

    def __call__(self,score: Score):
        buffer = BytesIO()
        writer(buffer,self.AVRO_SCHEMA,score.model_dump())
        return buffer.getvalue()
    