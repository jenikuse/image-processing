from PIL import Image

def median():
    path = 'noise.png' # image path
    name_out = 'mona_lisa.png'
    img = Image.open(path)
    width = img.size[0]
    height = img.size[1]

    members = [(0, 0)] * 9
    #newimg = Image.new("RGB", (width, height), "white")

    def median_cycle(img, members, count=1):
        print '\nmedian filter image processing...'

        for x in range (count):
            print 'step %i..' % (x+1)

            for i in range(1,width-1):
                for j in range(1,height-1):
                    members[0] = img.getpixel((i-1,j-1))
                    members[1] = img.getpixel((i-1,j))
                    members[2] = img.getpixel((i-1,j+1))
                    members[3] = img.getpixel((i,j-1))
                    members[4] = img.getpixel((i,j))
                    members[5] = img.getpixel((i,j+1))
                    members[6] = img.getpixel((i+1,j-1))
                    members[7] = img.getpixel((i+1,j))
                    members[8] = img.getpixel((i+1,j+1))
                    members.sort()
                    img.putpixel((i,j),(members[4]))
        return img

    #you can provide more iterations (need to add a number
    # after members argument in the next function). default is 1.
    # greater number takes more running time
    newimg = median_cycle(img, members)

    newimg.save(name_out)

    print '\nimage save as %s' % (name_out)