from utils.channel import Channel


def main():
    ch1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    ch2 = Channel('UC1eFXmJNkjITxPFWTy6RsWg')

    print(ch1)
    print(ch2)

    print(ch1 < ch2)
    print(ch1 > ch2)


if __name__ == '__main__':
    main()
