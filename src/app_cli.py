# entry point untuk ke mode cli atau command line interface ini kebutuhannya untuk development saja

from src.agents.lead import LeadAgent
from loguru import logger

lead_agent = LeadAgent()

def run():
    print(
        "Mentor Bahasa Inggris Virtual \n"
        "Coba tulis pesan: \n"
        "- Buatkan soal reading \n"
        "- Periksa: I goes to school \n"
        "- Berikan saya tips belajar \n"
        "Atau ngobrol bebas"
    )

    while True:
        prompt = input("[user]: ")

        if prompt.lower() == "/exit":
            break

        response = lead_agent.handle_send_message(user_id=101010, message_text=prompt)
        logger.debug(response)

        print(f"[AI]: {response["text"]}")

        if response["artifacts"]:
            artifacts_data = response["artifacts"].data
            for item in artifacts_data:
                logger.info(f"lokasi artifact: {item["artifact"]}")