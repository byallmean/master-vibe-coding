# Bao mat tich hop AI va LLM

File reference nay thuoc version 2.2. Chi load khi code cham toi AI API, LLM, prompt, tool calling hoac AI router nhu OpenRouter.

## API key cua AI chi o server

API key cua OpenAI, Anthropic, Google hay bat ky AI provider nao cung khong bao gio xuat hien o code client. Key lo co the dot hang nghin do trong vai phut. Moi AI call di qua backend: client gui noi dung toi server, server goi AI API.

## Spending cap va usage cap

Dat spending cap cung o moi AI provider trong dashboard cua provider. Them usage cap theo user trong app cua minh: theo doi token theo user trong database, dat cap ngay hoac thang theo user hoac theo goi, tra loi ro rang khi vuot cap. Khong chi dua vao cap cua provider vi cap do co the cap nhat cham.

## Prompt injection

User input phai duoc tach rieng khoi system prompt, khong noi thang input cua user vao system prompt. Dung message theo vai tro system va user tach biet thay vi noi chuoi.

Du vay, prompt injection tinh vi van co the xay ra. Voi ung dung quan trong thi them validate dau vao, validate output truoc khi hanh dong theo LLM, va gioi han kha nang cua LLM, vi du khong cho tool access doi voi chat user truc tiep.

## Output cua LLM la du lieu khong tin cay

Output cua LLM phai duoc coi nhu input cua user: sanitize truoc khi render thanh HTML vi output co the chua script hoac event handler, khong bao gio thuc thi output lam code neu khong co sandbox, va validate moi tham so tool call theo allowlist va schema truoc khi chay.

## Tool va function calling

Neu app cho LLM goi tool nhu query database, goi API hay thao tac file thi gioi han thao tac trong allowlist an toan, validate moi tham so tu LLM theo schema, dung quyen toi thieu, chi doc khi co the, log moi lan goi tool, va khong bao gio de LLM tu tao SQL tho hay lenh shell tu input cua user.
