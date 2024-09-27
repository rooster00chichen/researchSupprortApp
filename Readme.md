## ラズパイでのgpibの対応のさせ方
参考　https://zenn.dev/hroabe/articles/ceccb8ce114372
### 1.カーネルビルド
公式サイト（https://www.raspberrypi.com/documentation/computers/linux_kernel.html）を参考に、使用するモデルに合わせてInstall the kernelの項目までコマンドを実行する。
### 2.Linux-GPIB (GPIBドライバー)のビルド&インストール
svnのインストール
```svn install
sudo apt install subversion -y
sudo apt install automake libtool -y
```
kernelの所得
```
svn checkout svn://svn.code.sf.net/p/linux-gpib/code/trunk linux-gpib
```
make
```
cd linux-gpib
cd linux-gpib-kernel
make
sudo make install

cd ..
cd linux-gpib-user
 
./bootstrap
./configure
make
sudo make install
```
設定ファイルの用意と書き換え
```
sudo cp util/templates/gpib.conf /usr/local/etc/ 	
sudo vi /usr/local/etc/gpib.conf
```
書き換える内容
```
interface {
        minor = 0
        board_type = "ni_usb_b"
        name = "NI GPIB-USB-HS"
        pad = 0
        sad = 0
        timeout = T3s
        eos = 0x0a
        set-reos = yes
        set-bin = no
        set-xeos = no
        set-eot = yes
        base = 0
        irq  = 0
        dma  = 0
        master = yes
}

device {
        minor = 0
        name = "MSO6054A"
        pad = 1
        sad = 0
        eos = 0xa
        set-reos = no
        set-bin = no
}
```
書き換えたら以下を実行
```
sudo modprobe ni_usb_gpib
sudo ldconfig
sudo gpib_config
```
以下のコマンドを実行して問題なければOK(rebootを挟んだ方がいいかも？)
```
pi@raspberrypi:~ $ lsmod | grep gpib
ni_usb_gpib            40960  0
gpib_common            49152  1 ni_usb_gpib
```

### 3.pyvisaとpyvisa-pyのインストール
pyvisaとpyvisa-pyをpipから引っ張ってくる
