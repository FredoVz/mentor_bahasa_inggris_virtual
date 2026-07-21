# terdiri dari semua pada pydantic model
# bertugas untuk menangani hal-hal terkait struktur output pada setiap AI agents

# BaseModel adalah kelas yang akan diwarisi properti dan functionnya oleh setiap kelas-kelas yang lain atau skema yang lain
# Field untuk mendeskripsikan tiap properti secara detail 
# Literal akan membatasi nilai pada pilihan tertentu
from pydantic import BaseModel, Field
from typing import Literal

class ListeningExerciseSchema(BaseModel):
    speaker_one: str = Field(... , description="Nama pembicara pertama, misalnya: 'Joe'")
    speaker_two: str = Field(... , description="Nama pembicara kedua, misalnya: 'Jane'")
    script: str = Field(
        ... , 
        description="Dialog yang dibacakan oleh TTS (Text-to-Speech), format: 'Joe: ...\\nJane: ...' bergantian",
    )
    questions: list[str] = Field(
        ... , 
        description="Daftar pertanyaan untuk menguji pemahaman peserta berdasarkan `script`",
    )

class EvaluateUserIntentionSchema(BaseModel):
    skill_types: Literal["reading", "speaking", "writing", "listening"] = Field(
        ... , description="Pilihan salah satu skill_types yang dibutuhkan peserta"
    )

class LearningSkillTypesSchema(BaseModel): # item latihan yang dilakukan peserta
    category: str = Field(
        ... , 
        description="Salah satu kategori skill_types: reading, speaking, writing, dan listening",
    )
    title: str = Field(... , description="Judul latihan")
    feedback: str = Field(
        ... , description="Penilaian objective dengan metode sandwich feedback"
    )
    score: int = Field(... , description="Nilai kemampuan dalam rentang 1 - 10")

class LearningReportSchema(BaseModel): # laporan belajar
    start_date: str = Field(... , description="Tanggal mulai belajar")
    end_date: str = Field(... , description="Tanggal akhir belajar")
    username: str = Field(... , description="Username dari peserta")
    global_score: int = Field(... , description="Nilai keseluruhan")
    skill_types: list[LearningSkillTypesSchema] # list of LearningSkillTypesSchema
    markdown_content: str = Field(
        ... , description="Seluruh isi laporan dalam format markdown"
    )
