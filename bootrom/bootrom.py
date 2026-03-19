import bootrom.header_codes as hc
from hex_ops import HexValue

def calc_checksum():
    return 1

def boot_rom(rom):
    
    # read header
    correct_logo = 'ceed6666cc0d000b03730083000c000d0008111f8889000edccc6ee6ddddd999bbbb67636e0eecccdddc999fbbb9333e'
    rom_logo = rom[260:308].hex() # $0104 - $0133
    if rom_logo != correct_logo:
        raise Exception('ROM does not contain correct logo')
    print('Logo check passed')

    # report header values
    title = rom[308:324]
    print('Title: ',title)

    man_code = rom[319:323]
    print('Manufacturer code: ',man_code)

    cgb_flag = rom[323:324].hex()
    cgb_status = 'Supports CGB enhancements' if cgb_flag == '80' \
                    else 'CGB only' if cgb_flag == 'C0' \
                    else 'DMG'
    print('CGB flag: ', cgb_status)

    pc = HexValue('014B')
    olc = rom[pc.iget():pc.iget()+1].hex()
    if olc == '33':
        lc_hex = int('0144',16)
        liscensee_code_1 = rom[lc_hex:lc_hex+1].hex()
        liscensee_code_2 = rom[lc_hex+1:lc_hex+2].hex()
        try:
            liscensee_code = hc.new_liscensee_codes[liscensee_code_2]
        except:
            print(liscensee_code)
            liscensee_code = 'Publisher not found'
    else:
        liscensee_code = hc.old_liscensee_codes[olc]
    print('Liscensee code: ',liscensee_code)

    sgb_flag = rom[int('0146',16):int('0146',16)+1].hex()
    sgb_status = 'SGB supported' if sgb_flag == '03' else 'SGB unsupported'
    print(sgb_status)

    cart_type = rom[int('0147',16):int('0147',16)+1].hex()
    cart_type = '$'+str(cart_type)
    print('Cartridge type: ',hc.cartridge_types[cart_type])

    pc = HexValue('0147')
    pc.inc()
    rom_size = int(rom[pc.iget():pc.iget()+1].hex())
    print('ROM size: ',32*2**rom_size,' KiB')

    pc.inc()
    ram_type = rom[pc.iget():pc.iget()+1].hex()
    ram_type = '$'+str(ram_type)
    if hc.cartridge_types[cart_type].find('RAM') == -1 and ram_type != '$00':
        raise Exception('RAM inconsistency')
    print('RAM size: ',hc.ram_sizes[ram_type])

    pc.inc()
    dest = rom[pc.iget():pc.iget()+1].hex()
    dest = '$'+str(dest)
    print('Destination: ',hc.destination[dest])

    pc.inc() # Already handled old liscensee codes
    pc.inc()
    game_ver = rom[pc.iget():pc.iget()+1].hex()
    print('Game version: ', game_ver)

    pc.inc()
    checksum = rom[pc.iget():pc.iget()+1].hex()
    correct_checksum = calc_checksum()
    print('Header checksum: ', checksum)
    print('Checksum check not implemented.. sum')

    pc.inc()
    glob_check_1 = rom[pc.iget():pc.iget()+1].hex()
    pc.inc()
    glob_check_2 = rom[pc.iget():pc.iget()+1].hex()
    glob_check = glob_check_2 + glob_check_1
    print('Global checksum (not used): ', int(glob_check,16))

    return None