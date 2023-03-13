from utils.channel import Channel

def main():
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

    print(vdud.title)
    print(vdud.url)
    print(vdud.channel_view_count)

    vdud.__channel_id = 'New title'

    print(Channel.get_service())

    vdud.to_json('vdud.json')





if __name__ == '__main__':
    main()
