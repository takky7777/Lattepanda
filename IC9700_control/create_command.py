def createCommandArray():

    ##########CONFIG#######################

    #送信ヘッダCONFIG
    preamble_num = 30
    preamble_area = []

    #受信アドレスCONFIG
    receiver_address = 0xA2
    transmitter_address = 0xE0
    address_area=[]

    #コマンドエリアCONFIG
    command_area=[]

    #サブコマンドエリアCONFIG
    subcommand_area=[]

    #データエリアCONFIG
    data_area=[]

    #ポストアンブルエリアCONFIG
    postamble_area=[0xFD]




    #########CREATE FIELD##################

    #create preamble field
    preamble_area=[0xFE]*preamble_num

    #create address field
    address_area=[receiver_address,transmitter_address]

    #create command field
    command_area_value = input("Enter the command: ")
    command_area = [int(command_area_value, 16)]

    #create subcommand field
    subcommand_area_value = input("Enter the sub command: ")
    if subcommand_area_value:
        subcommand_area = [int(subcommand_area_value, 16)]
    else:
        subcommand_area = []

    #create data field
    data_area = [int(value, 16) for value in input("Enter the send data: ").split()]



    #########CREATE PACKET #################

    #create packet 
    command_array = preamble_area + address_area + command_area + subcommand_area + data_area + postamble_area

    return command_array