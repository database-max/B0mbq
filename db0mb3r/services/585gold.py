from db0mb3r.services.service import Service


class Zoloto585(Service):
    phone_codes = [998]

    async def run(self):
        await self.post(
            "https://customer.api.delever.uz/v1/customers/register",
            json={
                "name": self.russian_name,
                "phone": self.format(self.formatted_phone, "+* (***) ***-**-**"),
            },
        )
