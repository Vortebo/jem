import bootrom.header_codes as hc
from lowlevel.hex_ops import HexValue

def calc_checksum():
    return 1

def boot_rom(rom, pc):

    # TODO: display Nintendo logo (this'll be a while)
    
    # read header
    correct_logo = 'ceed6666cc0d000b03730083000c000d0008111f8889000edccc6ee6ddddd999bbbb67636e0eecccdddc999fbbb9333e'
    pc.value = '0104'
    rom_logo = rom.getrange(pc, 48)
    if rom_logo != correct_logo:
        print(rom_logo)
        raise Exception('ROM does not contain correct logo')
    print('Logo check passed')

    # report header values
    title = bytearray.fromhex(rom.getrange(pc, 16))
    title,man_code,cgb_flag=title[0:11].decode(),title[11:15].decode(),title[15:].hex()
    print('Title: ',title)

    # man_code = title[11:15].decode()
    print('Manufacturer code: ',man_code)

    # cgb_flag = title[15:]#rom[323:324].hex()
    cgb_status = 'Supports CGB enhancements' if cgb_flag == '80' \
                    else 'CGB only' if cgb_flag == 'C0' \
                    else 'DMG'
    print('CGB flag: ', cgb_status)

    liscensee_code_1 = rom.get(pc)
    liscensee_code_2 = rom.get(pc)
    try:
        liscensee_code = hc.new_liscensee_codes[liscensee_code_2]
    except:
        print(liscensee_code)
        liscensee_code = 'Publisher not found. May be old liscensee code.'
    print('New liscensee code: ',liscensee_code)

    sgb_flag = rom.get(pc)
    sgb_status = 'SGB supported' if sgb_flag == '03' else 'SGB unsupported'
    print(sgb_status)

    cart_type = rom.get(pc)
    cart_type = '$'+str(cart_type)
    print('Cartridge type: ',hc.cartridge_types[cart_type])

    rom_size = int(rom.get(pc))
    print('ROM size: ',32*2**rom_size,' KiB')

    ram_type = rom.get(pc)
    ram_type = '$'+str(ram_type)
    if hc.cartridge_types[cart_type].find('RAM') == -1 and ram_type != '$00':
        raise Exception('RAM inconsistency')
    print('RAM size: ',hc.ram_sizes[ram_type])

    dest = rom.get(pc)
    dest = '$'+str(dest)
    print('Destination: ',hc.destination[dest])

    olc = rom.get(pc)
    liscensee_code = hc.old_liscensee_codes[olc]

    game_ver = rom.get(pc)
    print('Game version: ', game_ver)

    checksum = rom.get(pc)
    correct_checksum = calc_checksum()
    print('Header checksum: ', checksum)
    print('Checksum check not implemented.. sum')

    glob_check_1 = rom.get(pc)
    glob_check_2 = rom.get(pc)
    glob_check = glob_check_2 + glob_check_1
    print('Global checksum (not used): ', int(glob_check,16))

    return pc, None