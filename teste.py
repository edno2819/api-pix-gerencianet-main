from services.pix import PixService



pix_service = PixService()
payload = pix_service.create_payload('1.00', "100cd4da-01d2-47f7-9ec2-00612f9eb22a")
qrcode = pix_service.create_cobranca("7978c0c87ea847e78ef5g49634473c1f1", payload)
qrcode