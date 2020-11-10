from cryptoadvance.specter.util.tx import *


def test_decoderawtransaction():
    hextx = "02000000000101902666609a245e45e426ead256ad47dca8a2b4dd65d1a634ad35b4a1c0603c0e0000000017160014c08fd0c4658b89678b9e0726838c2c2c2f41c3dffeffffff02b44d5a0300000000160014f81b3e69f5cafc2f1e69ed5625d07876e3558e6900e1f50500000000160014255fe80139657184c1de8e04f71c74c667dd7c3f02473044022038a29d1958d295a9739798c1a5f138404711d824f3bf103221d31bcbc11ff0010220635b4996de17290980c78e3de2547717de119e8312a52eb54fce73c27728c5e00121020356c34dd0931251a6e306704a912dbfeedb0f550a30a89689a1c8434cefa91000000000"
    res = decoderawtransaction(hextx, "regtest")
    assert res["size"] == 245
    assert res["vsize"] == 164
    assert res["weight"] == 653

    # coinbase tx
    hextx = "010000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff5f03a2030a1c2f5669614254432f4d696e656420627920736762756c6f686b79632f2cfabe6d6ded74726703908120aa4fa4f10557f50c66aa7419c7285edab024872b7bdd96bf1000000000000000101772a30fd92f0420e9dce2e133ebaa2affffffff0488b49929000000001976a914536ffa992491508dca0354e52f32a3a7a679a53a88ac00000000000000002b6a2952534b424c4f434b3a6f819a142bdad27916d8e8daf419907fa2cd7b085019d035823f3125002b83500000000000000000266a24b9e11b6d563b4d7c8486af0c15dac4c2764a39be25365cfb8990db6d170d794a562080660000000000000000266a24aa21a9ed256d453640cd18d3fe21bdc7f127e9c075e630b28be937a0c8e402807bc010360120000000000000000000000000000000000000000000000000000000000000000000000000"
    res = decoderawtransaction(hextx, "regtest")
    assert res["size"] == 362
    assert res["vsize"] == 335
    assert res["weight"] == 1340

    # legacy tx
    hextx = "020000000191f381c648c70f2388cce607f5955fe6b9f0b50a49c9bfa618413f931e55cf16000000006a4730440220543b92a31ed7cd00781cdce8cac4ef37fbfdce30a9dfc1f8e00a77f2dd35a2ec02201eb21ec97126f0dad8f0f066e0ae1cf44de8a3027caa99b819511ec57ba632c70121020f9c0041942551b00abcf1ba8d00f6ac93e67ddb378eecd0fb240a9ef3ddc9c0ffffffff0182480a010000000017a9143524696d526f50ab583c829bcca02553af9c64fa8700000000"
    res = decoderawtransaction(hextx, "regtest")
    assert res["size"] == 189
    assert res["vsize"] == 189
    assert res["weight"] == 756