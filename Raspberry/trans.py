#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Authors : Esma TALHI, Thomas GLUMINEAU
Documentation at : https://pyserial.readthedocs.io/en/latest/pyserial.html#
"""



def auto_detect_port():
    print("Scanning ports.")
    ser = serial.Serial(port="/dev/ttyS0",
                    baudrate=9600,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=1
                )
    print(type(ser))
    return ser



#Envoi d'une trame depuis Python vers Arduino en utilisant le port serie : ser
def send_trame(ser, trame: str):
    print(f"Sending trame: {trame}")
    data = trame.encode('utf-8')
    ser.write(data)
    #Sert à vider le buffer (qui contient la trame) et forcer python a envoyer les donnees immediatement
    ser.flush()
    print("Trame sent.")

#Reception d'une trame depuis Arduino vers Python en utilisant le port serie : ser
def reception_trame(ser):
    trame = ""
    print("Waiting for trame")
    while True:
        byte = ser.read(1)   # lire un octet
        #Si aucun ocetet n'est retourne, alors byte = b'' (chaine vide) consideree comme False en python
        if not byte:
            continue  # timeout → on continue
        char = byte.decode(errors="ignore")
        print(char, end="")
        trame += char

        if byte == b'\n':    # fin de trame
            break

    return trame


def main():
    #try:
    ser = auto_detect_port()
    #except Exception as e:
       # print(e)comports()
       # return

    while True:
        print("\n[1] - Envoyer une trame")
        print("[2] - Recevoir une trame")

        cmd = input("Choix: ")

        try:
            cmd = int(cmd)
        except:
            print("Commande invalide.")
            continue

        if cmd == 1:
            output_trame = "$ARDLM,456,38,0,B*6F\r\n"
            send_trame(ser, output_trame)

        elif cmd == 2:
            trame = reception_trame(ser)
            print("\nTrame reçue:", trame)

        else:
            print("Option inconnue.")


if __name__ == "__main__":
    main()
