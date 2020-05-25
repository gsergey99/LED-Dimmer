FIRMWARE = firmware

DEVICE = /dev/ttyACM0

STFLASH = st-flash

TEXT0_ADDR = 0x08000000
TEXT1_ADDR = 0x08020000
TEXT0_SECTIONS = .isr_vector
TEXT1_SECTIONS = .text .data




run:
	@python3 tools/pyboard.py --device $(DEVICE) blink_uPython/main.py

cpy:
	@python3 tools/pyboard.py --device $(DEVICE) -f cp blink_uPython/main.py :

rm:
	@python3 tools/pyboard.py --device $(DEVICE) -f rm main.py



deploy-stlink: $(FIRMWARE)/firmware.dfu
	@echo "Writing $(FIRMWARE)/firmware0.bin to the board via ST-LINK"
	$(STFLASH) write $(FIRMWARE)/firmware0.bin $(TEXT0_ADDR)
	@echo "Writing $(FIRMWARE)/firmware1.bin to the board via ST-LINK"
	$(STFLASH) --reset write $(FIRMWARE)/firmware1.bin $(TEXT1_ADDR)

reset:	
	@echo "Reset the board via ST-LINK"
	$(STFLASH) reset 

erase:	
	@echo "Erasing the board via ST-LINK"
	$(STFLASH) erase

