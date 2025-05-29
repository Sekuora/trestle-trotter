#include <iostream>
#include <filesystem>

using std::cout;
using std::endl;
using std::string;

int main()
{
    std::filesystem::path vessel_directory = ".vessel";
    std::filesystem::path externals_directory = ".vessel/externals";
    
    try
    {
        std::filesystem::create_directory(vessel_directory);
        std::filesystem::create_directory(externals_directory);

        cout << "Vessel environment created at: " << vessel_directory << "\n";
    }
    catch (const std::exception &e)
    {

        std::cerr << "Error creating Vessel: " << e.what() << '\n';
    }

    return 0;
}